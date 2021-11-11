#Esse código só funciona depois de já ter baixado o arquivo

import time
import pyautogui
import os
import random

print("INICIANDO...")
time.sleep(5)
print("BOT INICIADO!!")

#Atualizando o arquivo do repositório
os.chdir((os.path.realpath(__file__)) + "/../../musicas")
os.system("git pull")

#Abrindo o arquivo e dando o !add
f = open((os.path.realpath(__file__)) + "/../../musicas/musicas.txt",'r')
linhas = f.readlines()

#Até que enfim embaralhando a lista
random.shuffle(linhas)

for i in linhas:
	pyautogui.write("!add " + i)
	pyautogui.press("enter")
	time.sleep(1)