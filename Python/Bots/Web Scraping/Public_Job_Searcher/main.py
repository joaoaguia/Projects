# Libraries
import sys 
import os
from datetime import date, timedelta
import pandas as pd
import configparser

# Path to personal functions
sys.path.append((os.path.expanduser("~/Documents/Python_Project_Files/GIT/Functions")))
import Email_Sender
import Chromedriver
import Logs
import Web_Scrapper

# Path to data of the email sender
email_data = (os.path.expanduser("~/Documents/Python_Project_Files/Email/Email_data.txt"))
# Path to email receivers list
email_receiver = (os.path.expanduser("~/Documents/Python_Project_Files/Email/Receivers/Public_Job_Searcher/Public_Job_Searcher_Receivers.txt"))
# Path to Excel file to be stored
excel_path = (os.path.expanduser("~/Documents/Python_Project_Files/Excel_Files"))


# Name of the project will be used to fed the creation of the excel_files and logs folder
project_name = 'Public_Job_Searcher'

# Website used on the 'Web_Scrapper.scrap_data' that we're gonna web scrap
website = "https://www.bep.gov.pt/pages/oferta/Oferta_Pesquisa_basica.aspx"

# Table with the structure we want on our excel file
table = {'Código': [], 'Tipo Oferta': [], 'Vínculo': [], 'Carreira': [], 'Categoria': [], 'Distrito': [],
         'Organismo': [], 'Habilitações Literárias': [], 'Descrição da Habilitação Literária': [], 'Data Limite': [],
         'Remuneração': [], 'Suplemento Mensal': [], 'Requisitos de Nacionalidade': [], 'Link': []}
table_email = {'Link': []}

# Name of the Excel file
file_name = ('Extraction_' + date.today().strftime("%d_%m_%y") + '.xlsx')

# Create the excel files directory if it does not exist
directory = os.path.join(excel_path, project_name)
if not os.path.exists(directory):
    os.makedirs(directory)

# Email Info except email text, needs to be filled after 'Web_Scrapper.scrap_data'
config = configparser.ConfigParser()
config.read(email_receiver)
email_to = config['Email']['to']
email_bcc = config['Email']['bcc']
email_subject = ("Extração Concursos Publicos" + date.today().strftime(" %d-%m-%y"))
email_attachment = os.path.join(directory, file_name)

#Logger Initializer
logger = Logs.setup_logger(project_name)
logger.info("Starting the main program.")

logger.info("Starting Chromedriver.")
driver = Chromedriver.get_chromedriver()

logger.info("Initializing Web_Scrapper.")
rn_counter, ative_last_7days = (Web_Scrapper.scrap_data(driver, website, table, table_email))

logger.info("Saving Excel file.")
tabela_completa = pd.DataFrame(table)
tabela_completa.to_excel(os.path.join(directory, file_name))

logger.info("Initializing Email_Sender the main program.")

# Email message
email_text = ('''Boa tarde,

Segue em anexo os concursos públicos abertos para o dia''' + date.today().strftime(" %d-%m-%y") + '''

Existem ''' + str(rn_counter) +''' vagas que não requerem nacionalidade Portuguesa, ''' + str(ative_last_7days) +''' que vão expirar a ''' + (date.today() + timedelta(days=7)).strftime(" %d-%m-%y") +'''

Os links para os anúncios são:
''' + "\n".join(table_email['Link']) + '''

Obrigado
O melhor BOT do Mundo''')

logger.info(Email_Sender.send_email(email_to, email_bcc, email_subject, email_text, email_attachment, email_data))
logger.info("Finishing the main program.")
driver.close()
driver.quit()


