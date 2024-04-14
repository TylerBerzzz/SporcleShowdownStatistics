#Developed by: Tyler Bershad
#Assisted by: Chat GPT
#Last Modified: 4/14/2024
#Objective: Automatically scrape the sporcle data using Selenium for geography subject

import io
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Initialize the DataFrame
full_df = pd.DataFrame()

# Base URL with placeholders for the page number
base_url = "https://www.sporcle.com/user/steveylat/showdowns/{}?category=1&order_by=date-completed"

# Loop over page numbers from 1 to 9
for page_number in range(1, 10):  # up to 9, inclusive
    # Format URL with current page number
    url = base_url.format(page_number)
    driver.get(url)

    # Wait for the page to load using WebDriverWait
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    # Extract the page source and parse it with BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Extract the table
    table = soup.find('table')
    if table:
        data_io = io.StringIO(str(table))
        df = pd.read_html(data_io)[0]

        # Process "Steveylat's Results" if it exists in the DataFrame
        if "Steveylat's Results" in df.columns:
            print("TRUE")
            # Split "Steveylat's Results" into "Outcome" and "Percentage" based on the first space
            split_data = df["Steveylat's Results"].str.split(' ', 1, expand=True)
            df['Outcome'] = split_data[0]
            df['Percentage'] = split_data[1]
            # Optionally, remove the original "Steveylat's Results" column if no longer needed
            df.drop("Steveylat's Results", axis=1, inplace=True)

        # Append the processed DataFrame to the full DataFrame
        full_df = pd.concat([full_df, df], ignore_index=True)

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


