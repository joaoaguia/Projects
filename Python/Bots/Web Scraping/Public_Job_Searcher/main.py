# Libraries
import sys
import os
from datetime import date
import pandas as pd
from openpyxl import Workbook

import Email_Sender
import Chromedriver
import Logs
import Web_Scrapper

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)

directory = r'%s' % application_path+'\Excel_Files'

file_name = ('Extraction_' + date.today().strftime("%d_%m_%y") + '.xlsx')

table = {'Código': [], 'Tipo Oferta': [], 'Vínculo': [], 'Carreira': [], 'Categoria': [], 'Distrito': [],
         'Organismo': [], 'Habilitações Literárias': [], 'Descrição da Habilitação Literária': [], 'Data Limite': [],
         'Remuneração': [], 'Suplemento Mensal': [], 'Requisitos de Nacionalidade': []}

website = "https://www.bep.gov.pt/pages/oferta/Oferta_Pesquisa_basica.aspx"

email_to = "kama.florencio@gmail.com"
email_bcc = "joaopedroaguiadasilva@gmail.com"
email_subject = ("Extração Concursos Publicos" + date.today().strftime(" %d-%m-%y"))
email_attachment = os.path.join(directory, file_name)
email_data = 'D:/Particulares/Joao/Estudos/Programacao/GIT/Email_data.txt'

#Logger Initializer
logger = Logs.setup_logger(project_name='Public_Job_Searcher')
logger.info("Starting the main program.")

logger.info("Starting Chromedriver.")
driver = Chromedriver.get_chromedriver()

logger.info("Initializing Web_Scrapper.")
rn_counter=(Web_Scrapper.scrap_data(driver, website, table))

logger.info("Saving Excel file.")
tabela_completa = pd.DataFrame(table)
tabela_completa.to_excel(os.path.join(directory, file_name))

logger.info("Initializing Email_Sender the main program.")
email_text = ('''Boa tarde,

    Segue em anexo os concursos públicos abertos para o dia''' + date.today().strftime(" %d-%m-%y") + '''

    Existem ''' + str(rn_counter) +''' vagas que não requerem nacionalidade Portuguesa.

    Obrigado
    O melhor BOT do Mundo''')
logger.info(Email_Sender.send_email(email_to, email_bcc, email_subject, email_text, email_attachment, email_data))

logger.info("Finishing the main program.")
driver.close()
driver.quit()


