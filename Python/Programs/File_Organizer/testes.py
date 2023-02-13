import os # Lybrary Miscellaneous para a criação da pasta
import datetime
import Functions
import shutil # Library para copiar ficheiros
from PIL import Image # Library Pillow para a obtenção da data em que a foto foi tirada



path_origem = r"D:\Particulares\João\Estudos\Programação\Python\FILE_ORGANIZER\Files\Origem"
path_destino = r"D:\Particulares\João\Estudos\Programação\Python\FILE_ORGANIZER\Files\Destino"

for root, dirs, files in os.walk(path_origem):
        for name in files:
            path_file = (os.path.join(root,name))
            hash = (Functions.hash_file(path_file))
            #date=datetime.datetime.fromtimestamp(os.path.getmtime(path_file)).strftime('%Y-%m-%d') #Verifica a data de modificação do ficheiro em formato YYYY-MM-DD
            size = (Functions.convert_size(os.stat(path_file).st_size))

            #data = Image.open(path_file)._getexif()[36867] #Obtem a data e hora que foto foi tirada
            #print(data)
            try:
                data = Image.open(path_file)._getexif()[36867] #Obtem a data e hora que foto foi tirada
                print("--------try----------")
                print(name)
                print(data)
            except:

                #stat = os.stat(path_file)
                date=datetime.datetime.fromtimestamp(os.path.getmtime(path_file)).strftime('%Y-%m-%d')
                print("--------except----------")
                print(name)
                print(date)
              