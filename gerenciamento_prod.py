from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
import config
import json
import os

app_prod = Blueprint('cad_prod',__name__)

produtos = []

def gravar_produtos_arquivo():
    
    produtos_json = json.dumps(produtos)
    with open('banco.json', 'w') as arq:
        arq.write(produtos_json)

def ler_arquivo_json():
    global produtos
    with open('banco.json', 'r') as arq:
            produtos = json.load(arq)

def escrever_arquivo_json():
     with open('banco.json', 'w+') as arq:
            arq.write("[]")

def carregar_produtos_arquivo():
    global produtos

    try:
        ler_arquivo_json()

    except FileNotFoundError:
        escrever_arquivo_json()
        ler_arquivo_json()

carregar_produtos_arquivo()

def extensoes_permitidas(nome_arquivo):
    return '.' in nome_arquivo and nome_arquivo.rsplit('.', 1)[1].lower() in config.EXTENSOES

def ultimo_id_inserido():
    return produtos[-1]['id'] if len(produtos) != 0 else 0
            
def buscar_indice_produto(id):
    for indice, produto in enumerate(produtos):
            if produto['id'] == id:
                return indice, produto
    return -1, ""

@app_prod.route('/')
def home():
    return render_template('cadastro/home.html', produtos=produtos)

@app_prod.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == "POST":
        nome = request.form['nome']
        preco = float(request.form['preco'])
        quantidade = int(request.form['quantidade'])

        nome_arquivo = 'padrao.jpg'
        if 'foto' in request.files:
            foto = request.files['foto']
            if foto.filename != '':
                if foto and extensoes_permitidas(foto.filename):
                    nome_arquivo = secure_filename(foto.filename)
                    foto.save(os.path.join(config.UPLOAD_FOLDER, nome_arquivo))

        
        id = ultimo_id_inserido()

        produto = {
            "id": (id + 1), 
            "nome": nome, 
            "preco": preco,
            "quantidade": quantidade, 
            "foto": nome_arquivo
        }

        produtos.append(produto)

        gravar_produtos_arquivo()

        flash("Produto Cadastrado com Sucesso")
        return redirect('/')
    return render_template('cadastro/adicionar.html')

@app_prod.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    indice, produto_selecionado = buscar_indice_produto(id)

    if request.method == "POST":

        nome_arquivo = request.form['imagem']
        if 'foto' in request.files:
            foto = request.files['foto']
            if foto.filename != '':
                if foto and extensoes_permitidas(foto.filename):
                    nome_arquivo = secure_filename(foto.filename)
                    foto.save(os.path.join(config.UPLOAD_FOLDER, nome_arquivo))

        print(nome_arquivo)
        if indice != -1:
            produto = {
                "id": id, 
                "nome": request.form['nome'],
                "preco": float(request.form['preco']), 
                "quantidade": int(request.form['quantidade']),
                "foto": nome_arquivo
            }
            produtos[indice] = produto
        
        gravar_produtos_arquivo()
        flash("Produto Editado com Sucesso")

        return redirect('/')
            
    produto = {
        "id" : produto_selecionado['id'],
        "nome" : produto_selecionado['nome'],
        "preco" : produto_selecionado['preco'],
        "quantidade" : produto_selecionado['quantidade'],
        "foto" : produto_selecionado['foto'],
    }

    return render_template('cadastro/editar.html', produto=produto)

@app_prod.route('/excluir', methods=['POST'])
def excluir():
    indice, _ = buscar_indice_produto(int(request.form['id']))
    produtos.pop(indice)
    flash("Produto Excluído com Sucesso")
    return redirect('/')