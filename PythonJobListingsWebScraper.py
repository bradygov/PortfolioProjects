# Webscraping to build my own dataset

import requests
from bs4 import BeautifulSoup
import datetime
import csv 
import pandas as pd

# The website I'm scraping
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# Collecting the relevant data
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

# Creating the header for the .csv file
header = ['Job Title','Company','Location']

# wrting data to my newly created .csv file
with open('PythonJobListingsDataSet.csv','w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        data = [title_element.text.strip(),company_element.text.strip(),location_element.text.strip()]
        writer.writerow(data)

# Reading the file that was created
df = pd.read_csv(r'C:\Users\Brady\PythonJobListingsDataSet.csv')

print(df)