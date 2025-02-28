from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
from banco import produtos

app = Flask(__name__)
UPLOAD_FOLDER = '/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

@app.route('/')
def home():
    return render_template('home.html', produtos=produtos)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
                if foto and allowed_file(foto.filename):
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

@app.route('/excluir', methods=['POST'])
def excluir():

    id = int(request.form['id'])
    print(id)

    for indice, produto in enumerate(produtos):
        #print(indice, produto['id'], produto['nome'])
        print(type(produto['id']), type(id))
        if produto['id'] == id:
            print("Apagando indice:", indice)
            produtos.pop(indice)
            break
    print(produtos)
    return redirect('/')