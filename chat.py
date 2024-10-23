#projeto de chat
import os

mensagens = []

nome = input ("Nome: ")

while True:
    # limpando terminal
    os.system('cls') # windows: cls // linux/mac: clear

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("________________") #separar a lista de mensagens que será exibida com input

    # obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    # adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })