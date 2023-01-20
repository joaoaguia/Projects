# Libraries
import sys
import os
from datetime import date
import pandas as pd
# Path to personal functions
sys.path.append('D:/Particulares/Joao/Estudos/Programacao/GIT/Projects/Python/Functions')
import Email_Sender
import Chromedriver
import Logs
import Web_Scrapper

# Name of the project will be used to fed the creation of the excel_files and logs folder
project_name = 'Public_Job_Searcher'
# Website used on the 'Web_Scrapper.scrap_data' that we're gonna web scrap
website = "https://www.bep.gov.pt/pages/oferta/Oferta_Pesquisa_basica.aspx"
# Table with the structure we want on our excel file
table = {'Código': [], 'Tipo Oferta': [], 'Vínculo': [], 'Carreira': [], 'Categoria': [], 'Distrito': [],
         'Organismo': [], 'Habilitações Literárias': [], 'Descrição da Habilitação Literária': [], 'Data Limite': [],
         'Remuneração': [], 'Suplemento Mensal': [], 'Requisitos de Nacionalidade': []}
# Name of the Excel file
file_name = ('Extraction_' + date.today().strftime("%d_%m_%y") + '.xlsx')
# Create the excel files directory if it does not exist
directory = os.path.join("D:/Particulares/Joao/Estudos/Programacao/GIT/Excel_Files", project_name)
if not os.path.exists(directory):
    os.makedirs(directory)
# Email Info except email text, needs to be filled after 'Web_Scrapper.scrap_data'
email_to = "kama.florencio@gmail.com"
email_bcc = "joaopedroaguiadasilva@gmail.com"
email_subject = ("Extração Concursos Publicos" + date.today().strftime(" %d-%m-%y"))
email_attachment = os.path.join(directory, file_name)
email_data = 'D:/Particulares/Joao/Estudos/Programacao/GIT/Email_data.txt'

#Logger Initializer
logger = Logs.setup_logger(project_name)
logger.info("Starting the main program.")

logger.info("Starting Chromedriver.")
driver = Chromedriver.get_chromedriver()

logger.info("Initializing Web_Scrapper.")
rn_counter=(Web_Scrapper.scrap_data(driver, website, table))

logger.info("Saving Excel file.")
tabela_completa = pd.DataFrame(table)
tabela_completa.to_excel(os.path.join(directory, file_name))

logger.info("Initializing Email_Sender the main program.")
# Email message
email_text = ('''Boa tarde,

    Segue em anexo os concursos públicos abertos para o dia''' + date.today().strftime(" %d-%m-%y") + '''

    Existem ''' + str(rn_counter) +''' vagas que não requerem nacionalidade Portuguesa.

    Obrigado
    O melhor BOT do Mundo''')

logger.info(Email_Sender.send_email(email_to, email_bcc, email_subject, email_text, email_attachment, email_data))
logger.info("Finishing the main program.")
driver.close()
driver.quit()


