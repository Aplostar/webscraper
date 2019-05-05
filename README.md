A webscraper which uses python based selenium to access javascript rendered page. The site on which the scraper runs is https://techolution.app.param.ai/jobs/. 

Ensure while using the scraper to change the webdriver and it's path according to your preference.
  1) Change the path of variable CHROME_DRIVER_PATH
  2) Change the type of webdriver in driver = webdriver.Chrome(CHROME_DRIVER_PATH) if you want to use any other browser
The current code is for Chrome browser

The scraper uses selenium for data extraction. It accesses and finds the elements through their xpaths. After reading and processing the html texts of matching xpaths it writes this data into a csv file "data.csv" in order of date posted with the oldest post first and the latest post at the last. For processing the date posted content it uses dateparser library of python.

Installing necessary dependencies:
1) install selenium using :
   pip install -U selenium or conda install -c conda-forge selenium 

2) install dateparser using:
   pip install dateparser or conda install -c conda-forge dateparser
   
   
  
 
