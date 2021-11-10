import time
import pyautogui

print("INICIANDO...")
time.sleep(5)
print("BOT INICIADO!!")

f = open('musicas.txt','r')
linhas = f.readlines()

for i in linhas:
	pyautogui.write("!add " + i)
	pyautogui.press("enter")
	time.sleep(1)