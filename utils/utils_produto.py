from flask import session
import config
import json

def extensoes_permitidas(nome_arquivo):
    return '.' in nome_arquivo and nome_arquivo.rsplit('.', 1)[1].lower() in config.EXTENSOES

def ultimo_id_inserido(produtos):
    return produtos[-1]['id'] if len(produtos) != 0 else 0
            
def buscar_indice_produto(produtos, id):
    for indice, produto in enumerate(produtos):
            if produto['id'] == id:
                return indice, produto
    return -1, ""

def validar_sessao():
    try:
        if session['logado']:
            return True
    except:
        return False

def gravar_produtos_arquivo(produtos):
    produtos_json = json.dumps(produtos)
    with open('produtos.json', 'w') as arq:
        arq.write(produtos_json)

def ler_arquivo_json():
    produtos = []
    with open('produtos.json', 'r') as arq:
            produtos = json.load(arq)

    return produtos

def escrever_arquivo_json():
     with open('produtos.json', 'w+') as arq:
            arq.write("[]")

def carregar_produtos_arquivo():
    produtos = []

    try:
        produtos = ler_arquivo_json()

    except FileNotFoundError:
        escrever_arquivo_json()
        produtos = ler_arquivo_json()

    return produtos