# Sporcle Showdown 
## Overview
This project was inspired by our competitive Sporcle trivia games on Discord, where my friends and I noticed varying performance across different categories such as movies, sports, science, and geography. Curious for a deeper analysis beyond our anecdotal evidence, we found that Sporcle's raw stats didn't offer the insights we sought. This repository was created to fill that gap by enabling detailed performance analysis through data scraping.

## Objective
The aim is to demonstrate how to scrape Sporcle performance data for your account, specifically from the username tables, and analyze it in Python. This allows for a deeper understanding of strengths and weaknesses across different trivia categories.

## Methodology
As of April 11, 2024, this script is in its early stages, with only 30 minutes of development. Initial attempts to scrape Sporcle using the requests library were blocked, likely due to anti-scraping measures. The current method involves manually copying table data via the browser's "inspect" feature into a text file. A preliminary script successfully extracts this data for the "Science" category, serving as a proof of concept for further development.

### Step 1: 
Go to your Sporcle Username Page --> Showdowns and then change "All Categories" to the category of interest
![image](https://github.com/TylerBerzzz/SporcleShowdownStatistics/assets/30520534/f7507707-85cb-4b38-a31a-a916aaf8a2f6)

### Step 2: 
Right click anywhere on the table and select "Inspect"
![image](https://github.com/TylerBerzzz/SporcleShowdownStatistics/assets/30520534/5a6dc66c-c412-4e7f-ac9c-520295b4c39f)

### Step 3:
Select "<tbody> == $0 (2), and ensure the table values are highlighted (1). Next go to Copy (3) and select "Copy Element" 

### Step 4:
Open a notepad text file and paste the html information into it. Save it as "PageX.txt"

### Step 5:
Repeat the process for each page there.

## Result
Preliminary results after 30 min!

![image](https://github.com/TylerBerzzz/SporcleShowdownStatistics/assets/30520534/7426df04-b523-44c5-a323-cc609d0b43c3)
![image](https://github.com/TylerBerzzz/SporcleShowdownStatistics/assets/30520534/5b3a1c43-30c7-441d-b624-0a2ab49b0047)

## What's Next
Currently, the project offers a basic proof-of-concept model for extracting data on a single topic. The next step involves finding an efficient solution to bypass the manual data entry, with plans to explore the selenium library for automated web scraping.

