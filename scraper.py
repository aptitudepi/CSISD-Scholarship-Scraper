#!/usr/bin/env python

## Imports/Setup:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup

# Setup Webdriver (Using MSEdge webdriver distributed by Python's webdriver-manager package)
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Access the site using the driver:
driver.get('https://givetokids.csisd.org/programs/scholarships/')

# Locate Scholarship Name and Requirements:
scholarshipName = driver.find_elements(by=By.XPATH, value='//div[@class="collection-item-label"]')
scholarshipReqs = driver.find_elements(by=By.XPATH, value='//div[@class="collection-item-description"]')

# Create master dataframe
df = pd.DataFrame(columns=['Scholarship Name','Scholarship Requirements'])

## Data Processing
# Get scholarship names into an array
scholarshipNameList = []
for scholarship in range(len(scholarshipName)):
	scholarshipNameList.append(scholarshipName[scholarship].text)

# Get scholarship requirements into an array
scholarshipReqsList = []
for scholarship in range(len(scholarshipReqs)):
	if "\n" in scholarshipReqs[scholarship].text:
		soup = BeautifulSoup(scholarshipReqs[scholarship].text.split("\n")[1], "html.parser")
		for data in soup(['style', 'script']):
			data.decompose()
		soup = ' '.join(soup.stripped_strings)
		scholarshipReqsList.append(soup) # Get the part of the <p> element which is listed after "Scholarship Requirements", and strip all HTML tags

## Data Processing
# Add scholarship names and reqs into the dataframe
df['Scholarship Name'] = pd.Series(scholarshipNameList)
df['Scholarship Requirements'] = pd.Series(scholarshipReqsList)

## Data Export

# Uncomment to export to CSV
# df.to_csv('out/CSISDscholarships.csv')

# Uncomment to export to Excel
df.to_excel(r'out/CSISDscholarships.xlsx', sheet_name='Scholarships', index=False)
