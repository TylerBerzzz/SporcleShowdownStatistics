#Developed by: Tyler Bershad
#Assisted by: ChatGPT
#Last Modified: 4/14/2024
#Objective: Automatically scrape the sporcle data using Selenium for ALL sprocle subject

import io
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

# Categories for Sporcle
categories = {
    1: "GEOGRAPHY",
    2: "ENTERTAINMENT",
    3: "SCIENCE",
    4: "HISTORY",
    5: "LITERATURE",
    6: "SPORTS",
    7: "LANGUAGE",
    8: "JUST-FOR-FUN",
    9: "RELIGION",
    10: "MOVIES",
    11: "TELEVISION",
    12: "MUSIC",
    13: "GAMING",
    14: "MISCELLANEOUS",
    15: "HOLIDAY"
}

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Initialize the DataFrame
full_df = pd.DataFrame()

# Base URL without category specified yet
base_url_template = "https://www.sporcle.com/user/steveylat/showdowns/{}?category={}&order_by=date-completed"

# Loop over each category and their respective pages
for category_id, category_name in categories.items():
    page_number = 1
    max_page_number = 1  # Initially assume at least one page

    while page_number <= max_page_number:
        # Fetch each page
        url = base_url_template.format(page_number, category_id)
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # Extract the table
        table = soup.find('table')
        if table:
            data_io = io.StringIO(str(table))
            df = pd.read_html(data_io)[0]
            df['Category'] = category_name  # Add the category column
            full_df = pd.concat([full_df, df], ignore_index=True)

        # Update the max_page_number if necessary
        page_numbers = [int(div.text) for div in soup.find_all('div', class_='pagenum')]
        if page_numbers:
            max_page_number = max(page_numbers)

        page_number += 1

# Clean up
driver.quit()

# Splitting the 'steveylat's Results' into two columns
# Extracting the outcome (Lost/Won) and the percentage
full_df['Outcome'] = full_df["steveylat's Results"].str.extract(r'(\D+)')
full_df["steveylat's Results"] = full_df["steveylat's Results"].str.extract(r'(\d+%)')

# Cleaning up the 'Outcome' column to remove any extra spaces
full_df['Outcome'] = full_df['Outcome'].str.strip()

# Convert the 'steveylat's Results' and 'Opponent Results' columns from percentage strings to floats
full_df["steveylat's Results"] = full_df["steveylat's Results"].str.rstrip('%').astype(float)/ 100.0


full_df['Username'] = full_df['Opponent Results'].str.split().str[0]
full_df['Opponent Results'] = full_df['Opponent Results'].str.split().str[1]

full_df["Opponent Results"] = full_df["Opponent Results"].str.rstrip('%')
full_df["Opponent Results"] = pd.to_numeric(full_df["Opponent Results"], errors='coerce')
full_df["Opponent Results"] = full_df["Opponent Results"].fillna(0)
full_df["Opponent Results"] = full_df["Opponent Results"].astype(float)/ 100.0

#print(full_df)

# Provide statistics on the updated 'Steveylat\'s Results' and 'Opponent Results' columns
print("\nStatistics for 'Steveylat\'s Results':")
print(full_df["steveylat's Results"].describe())

print("\nStatistics for 'Opponent Results':")
print(full_df["Opponent Results"].describe())

# Calculate and print the number of wins, losses, and ties (if any)
outcome_counts = full_df['Outcome'].value_counts()

print(outcome_counts)

username_counts = full_df['Username'].value_counts()
print(username_counts)

print(full_df)
# full_df.to_excel("SporcleRecordScraped_4-14-2024.xlsx", index=False, engine='openpyxl')
# print("DataFrame is saved to Excel file successfully.")
