# Sporcle Showdown
## Last Modified: 4/14/2024
## This project is near complete! I will be rewritting everything to make it more clear soon.
## Overview
This project was inspired by our competitive Sporcle trivia games on Discord, where my friends and I noticed varying performance across different categories such as movies, sports, science, and geography. Curious for a deeper analysis beyond our anecdotal evidence, we found that Sporcle's raw stats didn't offer the insights we sought. This repository was created to fill that gap by enabling detailed performance analysis through data scraping.

Side note: if you want to play us, our username is **steveylat** :P

## Objective
The aim is to demonstrate how to scrape Sporcle performance data for your account, specifically from the username tables, and analyze it in Python. This allows for a deeper understanding of strengths and weaknesses across different trivia categories.

## Methodology
As of April 11, 2024, this script is in its early stages, with only 30 minutes of development. Initial attempts to scrape Sporcle using the requests library were blocked, likely due to anti-scraping measures. The  method involves manually copying table data via the browser's "inspect" feature into a text file. A preliminary script successfully extracts this data for the "Science" category, serving as a proof of concept for further development. The script is called *StatisticGrabber*

On April 14th @12PM, I tried out selenium for automatically retrieving the table from sporcle. It effectively collects information, it still needs improvements. For example, scraping all categories and iterating through each of its pages needs to be done in the next version. The script is called *AutomatedStatisticGrabber*

On April 14th @2:57AM, I've fully automated the retrieval for the **steveylat** username. The script is called *FullyAutomatedStatisticGrabber*

On April 14th @3:32PM, I've fully automated the retrieval for any username you're interested in selecting. I script is called *CompeitiveIntelligenceGrabber*. I also added graphing functionality as well. 


## Manual Scraping Method
### Step 1: 
Go to your Sporcle Username Page --> Showdowns and then change "All Categories" to the category of interest
![image](https://github.com/TylerBerzzz/SporcleShowdownStatistics/assets/30520534/f7507707-85cb-4b38-a31a-a916aaf8a2f6)

### Step 2: 
Right click anywhere on the table and select "Inspect"
![image](https://github.com/TylerBerzzz/SporcleShowdownStatistics/assets/30520534/5a6dc66c-c412-4e7f-ac9c-520295b4c39f)

### Step 3:
Select "<tbody> == $0 (2), and ensure the table values are highlighted (1). Next go to Copy (3) and select "Copy Element" 
![image](https://github.com/TylerBerzzz/SporcleShowdownStatistics/assets/30520534/a5091a1f-27cb-44b5-9492-0d66131f65b8)

### Step 4:
Open a notepad text file and paste the html information into it. Save it as "PageX.txt"

### Step 5:
Repeat the process for each page there.

## Result
Preliminary results after 30 min!

![image](https://github.com/TylerBerzzz/SporcleShowdownStatistics/assets/30520534/7426df04-b523-44c5-a323-cc609d0b43c3)
![image](https://github.com/TylerBerzzz/SporcleShowdownStatistics/assets/30520534/5b3a1c43-30c7-441d-b624-0a2ab49b0047)

## Automatic Scraping Method
Iterating through this url: **https://www.sporcle.com/user/steveylat/showdowns/{}?category=1&order_by=date-completed**
This part needs to be fixed because it's manually determined at the moment: *for page_number in range(1, 10):  # up to 9, inclusive*
![image](https://github.com/TylerBerzzz/SporcleShowdownStatistics/assets/30520534/26e669eb-de3c-4601-904f-efaa92b2130d)

## Fully Automatic Scraping Method
Everything is done through the hardcoded username!
![image](https://github.com/TylerBerzzz/SporcleShowdownStatistics/assets/30520534/2e324d4e-8add-48cd-9186-ba5fdd25bdfb)


## What's Next
Currently, the data is being properly collected and its only up from here! The final touches on this project will be to detatch the hard-coded username and make it dynamic.  

