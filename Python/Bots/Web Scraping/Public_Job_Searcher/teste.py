import sys
import os


#application_path = os.path.dirname(__file__)
#application_path = os.path.join(os.path.dirname(__file__)+"\Imagens")
#print(application_path)


application_path = os.path.join(os.path.dirname(__file__)+"\Imagens")


#os.chdir(os.path.join(os.path.dirname(__file__)+"\Imagens"))
teste = (os.path.dirname(__file__)+"\Imagens")
print(teste)

#os.chdir(teste)

#os.chdir(r'{}'.format(teste))
os.chdir(r'%s' % teste)