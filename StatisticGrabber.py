#Sprocle Statistic Grabber v1
#Last Modified: 4/11/2024
#Developer by: Tyler Bershad
#Assisted by GPT
'''
#Code objective: Derive user statistics from Sporcle Showdown by parsing by manual copying HTML information
from the associated pages. Sporcle does not allow page scraping, so manual scraping was the fastest initial path
to gathering initial data. For future automation, it may make sense to leverage selenium rather than the requests library
'''

from bs4 import BeautifulSoup
import pandas as pd

# Initialize an empty list to store the data from all files
data = []

# Loop through each file
for i in range(1, 7):  # For files page1.txt through page6.txt
    file_path = rf'Page{i}.txt'

    # Use a context manager to open and read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <tr> elements
    rows = soup.find_all('tr')
    for row in rows:
        # For each row, find all <td> elements
        cols = row.find_all('td')

        # Extract text from each column
        if len(cols) == 4:  # Ensure there are exactly 4 columns
            quiz_name = cols[0].find('a').text.strip()
            steveylat_result_raw = cols[1].text.strip()
            opponent_result = cols[2].find_all('div')[-1].text.strip()  # The last div contains the score
            date = cols[3].text.strip()

            # Split "Steveylat's Results" into outcome and percentage
            outcome, steveylat_percentage = steveylat_result_raw.split('\n')
            steveylat_percentage = steveylat_percentage.rstrip('%')

            # Append this row of data to our data list
            data.append([quiz_name, outcome, steveylat_percentage, opponent_result, date])

# Convert the list into a DataFrame
df = pd.DataFrame(data, columns=['Quiz', 'Outcome', 'Steveylat\'s Results', 'Opponent Results', 'Date'])

# Convert percentage strings to floats for calculation
df['Steveylat\'s Results'] = df['Steveylat\'s Results'].astype('float') / 100.0
df['Opponent Results'] = df['Opponent Results'].str.rstrip('%').astype('float') / 100.0

# Display the DataFrame with the new 'Outcome' column and updated 'Steveylat\'s Results'
print(df[['Outcome', 'Steveylat\'s Results', 'Opponent Results']])

# Provide statistics on the updated 'Steveylat\'s Results' and 'Opponent Results' columns
print("\nStatistics for 'Steveylat\'s Results':")
print(df['Steveylat\'s Results'].describe())

print("\nStatistics for 'Opponent Results':")
print(df['Opponent Results'].describe())

# Calculate and print the number of wins, losses, and ties (if any)
outcome_counts = df['Outcome'].value_counts()

print(outcome_counts)
