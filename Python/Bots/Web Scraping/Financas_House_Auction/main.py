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
email_receiver = (os.path.expanduser("~/Documents/Python_Project_Files/Email/Receivers/Financas_House_Auction/Financas_House_Auction_Receivers.txt"))
# Path to Excel file to be stored
excel_path = (os.path.expanduser("~/Documents/Python_Project_Files/Excel_Files"))


# Name of the project will be used to fed the creation of the excel_files and logs folder
project_name = 'Financas_House_Auction'

# Website used on the 'Web_Scrapper.scrap_data' that we're gonna web scrap
website = "https://vendas.portaldasfinancas.gov.pt/bens/consultaVendasCurso.action?tipoBem=02&tipoConsulta=*&modalidade=04&distrito=&concelho=&minimo=++.+++.+++.+++%2C++&maximo=++.+++.+++.+++%2C++&dataMin=&dataMax="

# Table with the structure we want on our excel file
table = {'Nº Venda': [], 'Preço Base de Venda': [], 'Data Limite para Propostas': [], 'Serviço de Finanças': [], 'Estado Actual': [], 'Modalidade': [], 'Link': []}

# Table that will go on the Email
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

email_subject = ("Leilão Finanças - Casas" + date.today().strftime(" %d-%m-%y"))
email_attachment = os.path.join(directory, file_name)

#Logger Initializer
logger = Logs.setup_logger(project_name)
logger.info("Starting the main program.")

logger.info("Starting Chromedriver.")
driver = Chromedriver.get_chromedriver()

logger.info("Initializing Web_Scrapper.")
ative_last_7days=(Web_Scrapper.scrap_data(driver, website, table, table_email))

logger.info("Saving Excel file.")
tabela_completa = pd.DataFrame(table)
tabela_completa.to_excel(os.path.join(directory, file_name))

logger.info("Initializing Email_Sender the main program.")

# Email message
email_text = ('''Boa tarde,

Segue em anexo os Leilões de casas / terrenos disponiveis no site das Finanças para o dia''' + date.today().strftime(" %d-%m-%y") + '''
Existem ''' + str(ative_last_7days) +''' Anuncios ativos que vão expirar até dia''' + (date.today() + timedelta(days=7)).strftime(" %d-%m-%y") +'''

Os links para os anúncios são:
''' + "\n".join(table_email['Link']) + '''

Obrigado
O melhor BOT do Mundo''')

logger.info(Email_Sender.send_email(email_to, email_bcc, email_subject, email_text, email_attachment, email_data))
logger.info("Finishing the main program.")
driver.close()
driver.quit()
