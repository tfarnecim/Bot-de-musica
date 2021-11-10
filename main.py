#bot do discord aqui pae

import discord
import time

def mostre(texto,comp):
    sobra = comp - len(texto)
    if(sobra < 0):
        return "INV"
    n1 = sobra//2
    n2 = sobra//2
    if(sobra%2!=0):
        n2+=1
    p1 = " "*n1
    p2 = " "*n2
    return p1 + texto + p2

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    '''FUNÇÕES PRA USAR NO CS'''

    if message.content.startswith('$lista'):
        f = open('musicas.txt','r')
        linhas = f.readlines()
        conteudo = "```\nMÚSICAS\n\n"
        cnt = 0
        for i in linhas:
            conteudo += "["+ str(cnt) + "]" + i
            cnt += 1
        conteudo += " \n```"
        f.close()
        await message.channel.send(conteudo)

    if message.content.startswith('$adiciona '):
        f = open('musicas.txt','a')
        musicanova = ""
        for i in range(10,len(message.content)):
            musicanova += message.content[i]
        f.write(musicanova+"\n")
        f.close()
        await message.channel.send("Música _" + musicanova + "_  adicionada com sucesso!!!")

    if message.content.startswith('$remove '):
        
        entrada = ""
        for i in range(8,len(message.content)):
            entrada += message.content[i]

        if(not entrada.isnumeric()):
            await message.channel.send("Especifique o número da música da lista que deve ser removida!!")            
            return 

        f = open('musicas.txt','r')
        lines = f.readlines()

        if(int(entrada) < 0 or int(entrada) > len(lines)):
            await message.channel.send("Posição da lista inválida!!")            
            return 
        
        f.close()
        del lines[int(entrada)]

        new_file = open("musicas.txt", "w+")

        for line in lines:
            new_file.write(line)

        new_file.close()
        await message.channel.send("Música removida com sucesso!!")

    '''FUNÇÕES PRA USAR COM SAMIRA'''

    if message.content.startswith('$l2'):
        f = open('musicas2.txt','r')
        linhas = f.readlines()
        conteudo = "```\nMÚSICAS\n\n"
        cnt = 0
        for i in linhas:
            conteudo += "["+ str(cnt) + "]" + i
            cnt += 1
        conteudo += " \n```"
        print(conteudo)
        f.close()
        await message.channel.send(conteudo)

    if message.content.startswith('$a '):
        f = open('musicas2.txt','a')
        musicanova = ""
        for i in range(3,len(message.content)):
            musicanova += message.content[i]
        f.write(musicanova+"\n")
        f.close()
        await message.channel.send("Música _" + musicanova + "_  adicionada com sucesso!!!")

    if message.content.startswith('$r '):
        
        entrada = ""
        for i in range(3,len(message.content)):
            entrada += message.content[i]

        if(not entrada.isnumeric()):
            await message.channel.send("Especifique o número da música da lista que deve ser removida!!")            
            return 

        f = open('musicas2.txt','r')
        lines = f.readlines()

        if(int(entrada) < 0 or int(entrada) > len(lines)):
            await message.channel.send("Posição da lista inválida!!")            
            return 
        
        f.close()
        del lines[int(entrada)]

        new_file = open("musicas2.txt", "w+")

        for line in lines:
            new_file.write(line)

        new_file.close()
        await message.channel.send("Música removida com sucesso!!")

    if message.content.startswith('$p '):
        entrada  = message.content
        entrada2 = ""
        for i in range(3,len(entrada)):
            entrada2+=entrada[i]

        musicas = ""
        atual = ""
        for i in range(len(entrada2)):
            if(entrada2[i] == ","):
                musicas += "!add " + atual+ "\n"
                atual = ""
                continue
            atual += entrada2[i]
        musicas += "!add " + atual
        await message.channel.send(musicas)

    if message.content.startswith('$letreiro '):
        
        mensagem = ""
        entrada = message.content

        for i in range(10,len(entrada)):
            mensagem += entrada[i]

        if(mostre(mensagem,55) == "INV"):
            return await message.channel.send("O comprimento da mensagem deve ser menor que 56 caracteres!!")

        await message.channel.send("```-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n" + "-                                                       -\n" + "-                                                       -\n" + "-"+mostre(mensagem,55)+"-\n" + "-                                                       -\n" + "-                                                       -\n" + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-```")


client.run("ODg4NTk1NDc0NTk1MDgyMjcw.YUU_Bg.cc90Q5JIp_qGHShFYDpjfHSPKZI")