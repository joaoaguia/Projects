from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime, timedelta
today = datetime.now()

def scrap_data(driver, website, table, table_email):
    ative_last_7days = 0
    rn_counter = 0
    counter = 0
    driver.get(website)
    try:
        # Wait for 10 sec for the search button to be present on the page
        search_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'ctl00$ctl00$FormMasterContentPlaceHolder$ContentPlaceHolder1$ucSearch')))

        # Check if the search button is enabled before clicking it
        if search_button.is_enabled():
            search_button.click()
        else:
            print("Search button is not enabled, cannot perform search.")

    except TimeoutException:
        print("Loading took too much time! Could not locate search button.")

    def extr_data():   
        ative_last_7days = 0
        rn_counter = 0
        # time.sleep(1)

        # here we have a away to find what element we want by entering in each other tag_name so we know that TR is inside TBODY and TBODY is inside MAIN
        # we could have done this with "find_element_by_xpath" and have only one variable defined
        main = driver.find_element(by=By.ID,value="ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_GvOfertaGestao")
        body = main.find_element(by=By.TAG_NAME, value='tbody')
        tr = body.find_elements(by=By.TAG_NAME, value='tr')
        var = 0

        for linha in tr:
            var = var + 1
            variable = str(var)
            # Extract the link element and add the text to the table
            link = driver.find_element(by=By.LINK_TEXT, value=(driver.find_element("xpath",f'/html/body/form[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/table/tbody/tr[{variable}]/td[1]').text))
            table['Código'].append(link.text)
            # Extract the text from the other cells and add it to the table
            table['Tipo Oferta'].append(driver.find_element("xpath",f'/html/body/form[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/table/tbody/tr[{variable}]/td[2]').text)
            table['Vínculo'].append(driver.find_element("xpath",f'/html/body/form[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/table/tbody/tr[{variable}]/td[3]').text)
            table['Carreira'].append(driver.find_element("xpath",f'/html/body/form[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/table/tbody/tr[{variable}]/td[4]').text)
            table['Categoria'].append(driver.find_element("xpath",f'/html/body/form[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/table/tbody/tr[{variable}]/td[5]').text)
            table['Distrito'].append(driver.find_element("xpath",f'/html/body/form[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/table/tbody/tr[{variable}]/td[6]').text)
            table['Organismo'].append(driver.find_element("xpath",f'/html/body/form[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/table/tbody/tr[{variable}]/td[7]').text)
            table['Habilitações Literárias'].append(driver.find_element("xpath",f'/html/body/form[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/table/tbody/tr[{variable}]/td[8]').text)
            date_string = driver.find_element("xpath",f'/html/body/form[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/table/tbody/tr[{variable}]/td[9]').text
            table['Data Limite'].append(date_string)

            #code of the offer
            print(link.text)
            link.click()

            try:
                rem = driver.find_element_by_id('ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_lblNORemuneracao').text
            except NoSuchElementException:
                rem = driver.find_element_by_id('ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_lblRemuneracao').text
            table['Remuneração'].append(rem)
            try:
                sm = driver.find_element_by_id('ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_lblNOSupMensal').text
            except NoSuchElementException:
                sm = driver.find_element_by_id('ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_lblSuplemento').text
            table['Suplemento Mensal'].append(sm)
            try:
                tab = driver.find_element(by=By.LINK_TEXT, value="Requisitos de Admissão")
                tab.click()
            except NoSuchElementException:
                pass
            try:
                dhl = driver.find_element_by_id('ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_lblDesHabLit').text
            except NoSuchElementException:
                try:
                    dhl = driver.find_element_by_id('ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_lblDescricaoHabilitacao').text
                except NoSuchElementException:
                    dhl = 'Não Indicado'
            table['Descrição da Habilitação Literária'].append(dhl)
            try:
                rn = driver.find_element_by_id('ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_lblNOReqNac').text
            except NoSuchElementException:
                try:
                    rn = driver.find_element_by_id('ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_lblRequisitosNacionalidade').text
                except NoSuchElementException:
                    rn = 'Não Indicado'
            table['Requisitos de Nacionalidade'].append(rn)
            if rn != 'Sim':
                rn_counter = rn_counter + 1
            
            table['Link'].append(driver.current_url)

            if rn != 'Sim' and datetime.strptime(date_string, '%Y-%m-%d') < today + timedelta(days=7):
                ative_last_7days += 1
                table_email['Link'].append(driver.current_url)
            
            driver.back()
        return (rn_counter, ative_last_7days)
    
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, ">")))
        while driver.find_element(by=By.LINK_TEXT, value='>').text == '>':
            counter = counter + 1
            print(counter)
            
            rn_counter_new, ative_last_7days_new = extr_data()
            rn_counter = rn_counter + rn_counter_new
            ative_last_7days = ative_last_7days + ative_last_7days_new

            driver.find_element(by=By.LINK_TEXT, value='>').click()

    except NoSuchElementException:
        counter = counter + 1
        print(counter)
        
        rn_counter_new, ative_last_7days_new = extr_data()
        rn_counter = rn_counter + rn_counter_new
        ative_last_7days = ative_last_7days + ative_last_7days_new
        return (rn_counter,ative_last_7days)