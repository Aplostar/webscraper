# Scraping using selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import dateparser
from bs4 import BeautifulSoup
import os
import csv


url = "https://techolution.app.param.ai/jobs/"

CHROME_DRIVER_PATH = '/chromedriver'
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url)
driver.implicitly_wait(100)
string = []
position = []

jobs = driver.find_elements_by_xpath("//*[@class='twelve wide computer twelve wide tablet sixteen wide mobile column']")
for job in jobs:
	string.append(job.text) 
newstring = []
for s in string:
	s = s.split('\n')
	position.append(s[0])
	s=s[1]
	newstring.append(s)
jobtype=[]
location = []
span = []
for s in newstring:
	s = s.split('·')
	jobtype.append(s[0])
	location.append(s[1])
	span.append(s[2])

dates = driver.find_elements_by_xpath("//*[@class='date_posted']")
dateposted = []
for date in dates:
	dateposted.append(date.text)
data=[]
for i in range(len(dateposted)):
	d = dateparser.parse(dateposted[i])
	data.append([dateposted[i],position[i],jobtype[i],location[i],span[i],d])

data.sort(key=lambda x:x[5])

with open('data.csv','w') as csvfile:
	fieldnames = ['DatePosted','Position','JobType','Location','Span']
	writer = csv.DictWriter(csvfile,fieldnames = fieldnames)

	writer.writeheader()
	for d in data:
		writer.writerow({'DatePosted':d[0],'Position':d[1],'JobType':d[2],'Location':d[3],'Span':d[4]})
