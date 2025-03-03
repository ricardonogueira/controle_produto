import json

def ler_arquivo_json():
    usuarios = []
    with open('usuarios.json', 'r') as arq:
            usuarios = json.load(arq)
    return usuarios

def escrever_arquivo_json():
     with open('usuarios.json', 'w+') as arq:
            arq.write("[]")

def carregar_usuarios_arquivo():
    usuarios = []

    try:
        usuarios = ler_arquivo_json()

    except FileNotFoundError:
        escrever_arquivo_json()
        usuarios = ler_arquivo_json()
    
    return usuarios