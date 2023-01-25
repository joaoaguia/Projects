import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# Path to personal functions
sys.path.append('D:/Particulares/Joao/Estudos/Programacao/GIT/Projects/Python/Functions')
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

# Use the webdriver to request the page
driver.get(website)

# Wait for the page to load
time.sleep(5)
driver.implicitly_wait(10)

# Get the page source
html = driver.page_source

table = {'Destrito': [], 'Nº Imoveis': [], 'Link': []}


main = driver.find_element(By.TAG_NAME, "ul")
print(main)





'''
var = 0

while var < 29:
        var = var + 1
        variable = str(var)
        print(var)
        try:
                table['Nº Imoveis'].append(driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/nav[2]/ul/li[{variable}]/div').text)
                table['Destrito'].append(driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/nav[2]/ul/li[{variable}]/a').text)
                table['Link'].append(driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/nav[2]/ul/li[{variable}]/a').get_attribute("href"))

        except NoSuchElementException:
                table['Nº Imoveis'].append(driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/nav[2]/ul/li[{variable}]/span').text)
                table['Destrito'].append(driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div/nav[2]/ul/li[{variable}]/text()'))

print (table)
#/html/body/div[2]/div/div/div/nav[2]/ul/li[7]/text()
/html/body/div[2]/div/div/div/nav[2]/ul/li[7]/text()
#/html/body/div[2]/div/div/div/nav[2]/ul/li[7]/text()
#/html/body/div[2]/div/div/div/nav[2]/ul/li[7]/text()
#/html/body/div[2]/div/div/div/nav[2]/ul/li[20]/text()
#/html/body/div[2]/div/div/div/nav[2]/ul/li[7]/span

            
'''


