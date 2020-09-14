import os
from zipfile import ZipFile 
import time
from selenium import webdriver
import requests
import urllib.request
import lxml

url = 'https://s3.amazonaws.com/tripdata/index.html'
chrome_driver_path = 'chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)
time.sleep(3)
links = driver.find_element_by_tag_name('a')
driver.quit()
print(links.href)
# zip_file_path = ('Zip_Data')
# zip_file_names = os.listdir(zip_file_path)

# for file in zip_file_names:
#     with ZipFile(f'Zip_Data/{file}', 'r') as zip:
#         zip.extractall('Monthly_Data')