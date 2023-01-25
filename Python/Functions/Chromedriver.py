#********************************************************
#Program:       Chromedriver
#Description:   This scrypt is resposible to call Chromedriver, check and download latest version of chromedriver, and return a headless chromedriver
#********************************************************

#Libraries
from selenium import webdriver
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_chromedriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    
    return driver


def get_chromedriver_undetected():

    options = webdriver.ChromeOptions()

    #options.add_argument("user-agent=[Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36]")
  
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')
    #options.add_argument('--no-sandbox')
    #options.add_argument('start-maximized')
    #options.add_argument('disable-infobars')
    #options.add_argument('--disable-dev-shm-usage')
    #options.add_argument('--remote-debugging-port=9222')
    #driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver = uc.Chrome(options=options)
    
    return driver