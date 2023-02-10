# Libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime, timedelta
today = datetime.now()


def scrap_data(driver, website, table, table_email):
    ative_last_7days = 0
    counter = 0
    driver.get(website)
    try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'header-logo-element')))

    except TimeoutException:
            print("Loading took too much time!")
    def extr_data():
        ative_last_7days = 0
        var = 6
        for i in range(0,10):
                var += 1
                variable = str(var)
                try:
                        table['Nº Venda'].append(driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[2]').text)
                        try:
                                table['Preço Base de Venda'].append(float(driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[4]').text.replace('.','').replace('€','').replace(',','.')))
                        except ValueError:
                                table['Preço Base de Venda'].append(driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[4]').text)

                        date_string = driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[6]').text
                        table['Data Limite para Propostas'].append(date_string)
                        table['Serviço de Finanças'].append(driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[8]').text)

                        status = driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[10]').text
                        table['Estado Actual'].append(status)
                        table['Modalidade'].append(driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[2]/td[1]/span[12]').text)
                        table['Link'].append(driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[1]/td[3]/table/tbody/tr/th[1]/a').get_attribute('href'))
                        
                        if status == 'Em Curso' and datetime.strptime(date_string, '%Y-%m-%d às %H:%M') < today + timedelta(days=7):
                                ative_last_7days += 1
                                table_email['Link'].append(driver.find_element_by_xpath(f'/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[{variable}]/td/div/table/tbody/tr[1]/td[3]/table/tbody/tr/th[1]/a').get_attribute('href'))
                except NoSuchElementException:
                        break

        return ative_last_7days

    try:
        while driver.find_element_by_xpath('//img[@alt="Próximo"]').get_attribute('alt') == 'Próximo':
            counter = counter + 1
            print("Page", counter)
            ative_last_7days = extr_data() + ative_last_7days
            driver.find_element_by_xpath('//img[@alt="Próximo"]').click()

    except NoSuchElementException:
            counter = counter + 1
            print("Page", counter)
            ative_last_7days = extr_data() + ative_last_7days
            return (ative_last_7days)
 