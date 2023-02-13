import os # Lybrary Miscellaneous para a criação da pasta
import shutil # Library para copiar ficheiros
import calendar # Library para a conversão de numero em mês
import datetime
import math
import hashlib # Library para a criação de HASH de um ficheiro
import time
def getHora():
    hora = time.localtime()
    formatHora = time.strftime("%H:%M:%S", hora)
    return formatHora

#CRIA PASTAS
def create_folders(path_destino, data):
    # Cria a pasta do Ano
    dir = os.path.join(path_destino,data[0:4])
    if not os.path.exists(dir):
        os.mkdir(dir)
    # Cria a pasta do mês dentro do ano
    dir = os.path.join(path_destino, data[0:4],(data[5:7])+" - "+calendar.month_name[int(data[5:7])])
    if not os.path.exists(dir):
        os.mkdir(dir)
    # Cria a pasta do dia dentro do mês e Ano
    #dir = os.path.join(path_destino, data[0:4], (data[5:7])+" - "+calendar.month_name[int(data[5:7])], data[8:10])
    #if not os.path.exists(dir):
    #    os.mkdir(dir)
    return(dir)

#CONVERTE BYTES NA RESPETIVA CONVERSÂO
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

#CRIA CODIGO HASH
def hash_file(path_file):
            h = hashlib.sha1()  # Criação de um ficheiro HASH
            with open(path_file, 'rb') as file:  # Abre o ficheiro em reading em modo binario
                chunk = 0  # loop até ao final do ficheiro
                while chunk != b'':
                    chunk = file.read(1024)  # Lê somente 1024 bytes de cada vez
                    h.update(chunk)
            return h.hexdigest()

#DUPLICADOS
#def duplicated (hash):



