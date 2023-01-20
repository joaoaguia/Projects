#********************************************************
#Program:       Chromedriver
#Description:   This scrypt is resposible to call Chromedriver, check and download latest version of chromedriver, and return a headless chromedriver
#********************************************************

#Libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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