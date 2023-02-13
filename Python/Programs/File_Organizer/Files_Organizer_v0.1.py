import os # Lybrary Miscellaneous para a criação da pasta
import shutil # Library para copiar ficheiros
import datetime
import Functions
from pathlib import Path
from PIL import Image # Library Pillow para a obtenção da data em que a foto foi tirada

hash_list=[]
path_origem = r"D:\Particulares\João\Estudos\Programação\Python\FILE_ORGANIZER\Files\Origem"
path_destino = r"D:\Particulares\João\Estudos\Programação\Python\FILE_ORGANIZER\Files\Destino"
#-----------------------
#path_origem = r"C:\Users\joao_\Desktop\FOTOS_KAMINSKI"
#path_destino = r"D:\Particulares\Fotos"
#-----------------------
#path_origem = r"C:\Users\joao_\Desktop\FOTOS_KAMINSKI"
#path_destino = r"D:\Particulares\Fotos_Tratado"

txt_duplicated = os.path.join(path_destino,"Duplicados","Duplicados.txt") # diretoria e nome do txt de duplicados
txt_hash = os.path.join(path_destino,"Hash.txt") # diretoria e nome do txt de hash
logs = os.path.join(path_destino,"Logs.txt") # diretoria e nome do txt de hash

choice = 1

if choice == 1:

    #Check se existe Hash.txt no destino
    if Path(txt_hash).is_file():
        with open(txt_hash) as f:
            hash_list = f.read().splitlines() 
            print(f"debug ({Functions.getHora()}): Hash.txt Existe ({txt_hash})")

    #Move Ficheiros para sua respetiva pasta
    for root, dirs, files in os.walk(path_origem):
        for name in files:
            path_file = (os.path.join(root,name))
            hash = (Functions.hash_file(path_file))
            size = (Functions.convert_size(os.stat(path_file).st_size))
            #date=datetime.datetime.fromtimestamp(os.path.getmtime(path_file)).strftime('%Y-%m-%d') #Verifica a data de modificação do ficheiro em formato YYYY-MM-DD

            try:
                date = Image.open(path_file)._getexif()[36867] #Obtem a data e hora que foto foi tirada
            except:
                date=datetime.datetime.fromtimestamp(os.path.getmtime(path_file)).strftime('%Y-%m-%d')
            
            if hash not in hash_list:
                txt_h = open(txt_hash,"a+")      
                txt_h.write(hash + '\n')
                #Chama a função de criação de Pastas
                Functions.create_folders(path_destino,date)
                #Move os ficheiros para a nova diretoria criada
                try:
                    print(shutil.move(path_file, Functions.create_folders(path_destino,date)))
                    shutil.move(path_file, Functions.create_folders(path_destino,date))
                    print(f"debug ({Functions.getHora()}): Ficheiro Movido ({name})")
                    txt_l = open(logs,"a+")            # a+ cria um novo ficheiro e vai fazendo append das linhas umas em baixo das outras
                    txt_l.write(f'debug ({Functions.getHora()}): Ficheiro Movido ({name})\n')
                    hash_list.append(hash)
                except:
                    print("ERRO")
                    break

            else:


                duplicated_files = os.path.join(path_destino, "Duplicados")
                if not os.path.exists(duplicated_files):
                    os.mkdir(duplicated_files)
                shutil.move(path_file, os.path.join(duplicated_files, name))
                txt_d = open(txt_duplicated,"a+")            # a+ cria um novo ficheiro e vai fazendo append das linhas umas em baixo das outras
                txt_d.write(f'{name}     {size}     {date}     {os.path.join(path_destino, date)}\n')
                print(f"debug ({Functions.getHora()}): Duplicado ({name})")

                txt_l = open(logs,"a+")            # a+ cria um novo ficheiro e vai fazendo append das linhas umas em baixo das outras
                txt_l.write(f'debug ({Functions.getHora()}): Duplicado ({name})\n')



if choice == 0:
    #Reverter a movimentação para a pasta de origem
    #os.remove(os.path.join(path_destino,"Duplicados","Duplicados.txt"))
    #os.remove(os.path.join(path_destino,"Hash.txt"))
    for root, dirs, files in os.walk(path_destino):
        for name in files:
            path_file = (os.path.join(root,name))
            #Move os ficheiros para a nova diretoria criada
            shutil.move(path_file, path_origem)
    #Apaga as pastas dentro da pasta destino
    for filename in os.listdir(path_destino):
        shutil.rmtree(os.path.join(path_destino, filename))

print("Ficheiros Movidos")



            

    
    





   