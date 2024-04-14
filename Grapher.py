#Developed by: Tyler Bershad
#Assisted by: ChatGPT
#Last Modified: 4/14/2024
#Objective: Graph test of cumulative wins and losses over time

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
file_path = 'SporcleRecordScraped_4-14-2024.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Ensure the 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group by date and outcome to count occurrences of each outcome
outcome_counts = df.groupby(['Date', 'Outcome']).size().unstack(fill_value=0)

# Calculate the daily difference between wins and losses
outcome_counts['Difference'] = outcome_counts.get('won', 0) - outcome_counts.get('lost', 0)

# Calculate the cumulative difference over time
outcome_counts['Cumulative Difference'] = outcome_counts['Difference'].cumsum()

# Plotting the cumulative difference over time
plt.figure(figsize=(12, 6))
plt.plot(outcome_counts.index, outcome_counts['Cumulative Difference'], marker='o', linestyle='-', color='blue')
plt.title('Cumulative Difference Between Wins and Losses Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Difference (Wins - Losses)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8)  # Add a line at zero for reference
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout for better display
plt.show()
