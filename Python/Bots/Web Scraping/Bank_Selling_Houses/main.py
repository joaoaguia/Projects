import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from datetime import date
import pandas as pd
import os


# Path to personal functions
sys.path.append('C:\Users\Kaminski\Desktop\Joao\GIT\Projects\Python\Functions')
#import Email_Sender
import Chromedriver
import Logs
#import Web_Scrapper

# Name of the project will be used to fed the creation of the excel_files and logs folder
project_name = 'Financas_House_Auction'
# Website used on the 'Web_Scrapper.scrap_data' that we're gonna web scrap
website = "https://www.idealista.pt/imoveis-da-banca"

#Logger Initializer
logger = Logs.setup_logger(project_name)
logger.info("Starting the main program.")

logger.info("Starting Chromedriver.")
driver = Chromedriver.get_chromedriver_undetected()
driver.save_screenshot('selenium-datadome.png')

# Use the webdriver to request the page
driver.get(website)

# Wait for the page to load
time.sleep(10)
driver.implicitly_wait(10)

try:
        agree = driver.find_element(By.XPATH, f'//*[@id="didomi-notice-agree-button"]/span')
        agree.click()
except NoSuchElementException:
        print('No Agree Button Presented')

# Get the page source
html = driver.page_source

table = {'Destrito': [], 'Nº Imoveis': [], 'Link': []}

# Name of the Excel file
file_name = ('Extraction_' + date.today().strftime("%d_%m_%y") + '.xlsx')
# Create the excel files directory if it does not exist
directory = ("C:/Users/Kaminski/Desktop/Joao/GIT/Projects/Python/Bots/Web Scraping/Bank_Selling_Houses")

li_elements = driver.execute_script("return document.querySelectorAll('nav#search-bylocation ul.citiesList.locations.clearfix li');")

print(li_elements)
count = len(li_elements)
print (count)

var = 0
for li in li_elements:
        var = var + 1
        variable = str(var)
        print(var)
        try:
                table['Nº Imoveis'].append(driver.find_element(By.XPATH, f'//*[@id="search-bylocation"]/ul/li[{variable}]/div').text)
                table['Destrito'].append(driver.find_element(By.XPATH, f'//*[@id="search-bylocation"]/ul/li[{variable}]/a').text)
                #Link = driver.find_element(By.XPATH, f'//*[@id="search-bylocation"]/ul/li[{variable}]/a').get_attribute("href")
                #table['Link'].append(Link)
                element = driver.find_element(By.XPATH, f'//*[@id="search-bylocation"]/ul/li[{variable}]/a')
                link = element.get_attribute("href")
                table['Link'].append(link)
                element.click()
                time.sleep(1)
                driver.back()
                time.sleep(1)
                
        except NoSuchElementException:
                table['Nº Imoveis'].append(driver.find_element(By.XPATH, f'//*[@id="search-bylocation"]/ul/li[{variable}]/span').text)
                Destrito = driver.find_element(By.XPATH, f'//*[@id="search-bylocation"]/ul/li[{variable}]').text
                Destrito = Destrito.replace('0\n','')
                table['Destrito'].append(Destrito)
                table['Link'].append('')

tabela_completa = pd.DataFrame(table)
tabela_completa.to_excel(os.path.join(directory, file_name))


print(table)
