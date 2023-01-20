# Libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def scrap_data(driver, website, table):
    counter = 0
    driver.get(website)
    try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'header-logo-element')))

    except TimeoutException:
            print("Loading took too much time!")
    def extr_data():
                    var = 6
                    for i in range(0,10):
                            var = var + 1
                            variable = str(var)
                            try:
                                    table['Nº Venda'].append(driver.find_element_by_xpath(
                                            f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[2]').text)
                                    table['Preço Base de Venda'].append(driver.find_element_by_xpath(
                                            f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[4]').text)
                                    table['Data Limite para Propostas'].append(driver.find_element_by_xpath(
                                            f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[6]').text)
                                    table['Serviço de Finanças'].append(driver.find_element_by_xpath(
                                            f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[8]').text)
                                    table['Estado Actual'].append(driver.find_element_by_xpath(
                                            f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[10]').text)
                                    table['Modalidade'].append(driver.find_element_by_xpath(
                                            f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[12]').text)
                                    table['Link'].append(driver.find_element_by_xpath(
                                    f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[1]/td[3]/table/tbody/tr/th[1]/a').get_attribute('href'))

                            except NoSuchElementException:
                                    break

    try:
        while driver.find_element_by_xpath('//img[@alt="Próximo"]').get_attribute('alt') == 'Próximo':
            counter = counter + 1
            print("Page", counter)
            extr_data()

            driver.find_element_by_xpath('//img[@alt="Próximo"]').click()

    except NoSuchElementException:
            counter = counter + 1
            print("Page", counter)
            extr_data()
 