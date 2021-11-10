#Esse código só funciona pra baixar o repositório caso não tenha baixado ainda

import time
import os

print("INICIANDO...")
time.sleep(5)
print("BOT INICIADO!!")

#Clonando o repositório
os.chdir((os.path.realpath(__file__)) + "/../../")
os.system("git clone https://github.com/tfarnecim/musicas.git")