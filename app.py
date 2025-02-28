from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
from banco import produtos

app = Flask(__name__)
UPLOAD_FOLDER = os.path.abspath('static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

EXTENSOES = {'png', 'jpg', 'jpeg'}

@app.route('/')
def home():
    return render_template('home.html', produtos=produtos)

def extensoes_permitidas(nome_arquivo):
    return '.' in nome_arquivo and nome_arquivo.rsplit('.', 1)[1].lower() in EXTENSOES


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == "POST":
        nome = request.form['nome']
        preco = request.form['preco']
        quantidade = request.form['quantidade']

        nome_arquivo = 'padrao.jpg'
        if 'foto' in request.files:
            foto = request.files['foto']
            if foto.filename != '':
                if foto and extensoes_permitidas(foto.filename):
                    nome_arquivo = secure_filename(foto.filename)
                    foto.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo))

        ultimo_id = produtos[-1]['id']

        produtos.append({
            "id": ultimo_id + 1,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "foto": nome_arquivo
        })

        return redirect('/')
    return render_template('adicionar.html')

def buscar_indice_produto(id):
    for indice, produto in enumerate(produtos):
            if produto['id'] == id:
                return indice, produto
    return -1, ""

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    indice, produto_selecionado = buscar_indice_produto(id)

    if request.method == "POST":

        nome_arquivo = request.form['imagem']
        if 'foto' in request.files:
            foto = request.files['foto']
            if foto.filename != '':
                if foto and extensoes_permitidas(foto.filename):
                    nome_arquivo = secure_filename(foto.filename)
                    foto.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo))

        if indice != -1:
            produtos[indice] = {
                "id": id,
                "nome": request.form['nome'],
                "preco": request.form['preco'],
                "quantidade": request.form['quantidade'],
                "foto": nome_arquivo
            }
    
        return redirect('/')
            
    produto = {
        "id" : produto_selecionado['id'],
        "nome" : produto_selecionado['nome'],
        "preco" : produto_selecionado['preco'],
        "quantidade" : produto_selecionado['quantidade'],
        "foto" : produto_selecionado['foto'],
    }

    return render_template('editar.html', produto=produto)

@app.route('/excluir', methods=['POST'])
def excluir():

    indice, _ = buscar_indice_produto(int(request.form['id']))
    produtos.pop(indice)

    return redirect('/')