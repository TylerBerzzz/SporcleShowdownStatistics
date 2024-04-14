#Developed by: Tyler Bershad
#Assisted by: ChatGPT
#Last Modified: 4/14/2024
#Objective: Graph test of cumulative wins and losses by category over time

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the Excel file
file_path = 'SporcleRecordScraped_4-14-2024.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Ensure the 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group by date, category, and outcome
category_outcome_counts = df.groupby(['Date', 'Category', 'Outcome']).size().unstack(fill_value=0)

# Calculate the daily difference between wins and losses for each category
category_outcome_counts['Difference'] = category_outcome_counts.get('won', 0) - category_outcome_counts.get('lost', 0)

# Drop unnecessary columns to keep only the difference
category_outcome_counts = category_outcome_counts[['Difference']].reset_index()

# Pivot the data so categories are columns and dates are rows
category_differences = category_outcome_counts.pivot_table(index='Date', columns='Category', values='Difference', fill_value=0)

# Calculate the cumulative sum of differences for each category
cumulative_category_differences = category_differences.cumsum().reset_index()

# Melt the DataFrame for easier plotting with Seaborn
cumulative_category_differences_melted = cumulative_category_differences.melt(id_vars=['Date'], var_name='Category', value_name='Cumulative Difference')

# Set the color palette
palette = sns.color_palette("hsv", len(cumulative_category_differences.columns) - 1)

# Plotting with Seaborn
plt.figure(figsize=(14, 8))
sns.lineplot(data=cumulative_category_differences_melted, x='Date', y='Cumulative Difference', hue='Category', palette=palette, marker="o")

plt.title('Cumulative Difference Between Wins and Losses Per Category Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Difference (Wins - Losses)')
plt.grid(True)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc=2)
plt.xticks(rotation=45)
plt.tight_layout(rect=[0, 0, 0.85, 1])  # Adjust layout to fit the legend outside the plot
plt.show()
