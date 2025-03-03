from flask import Blueprint, render_template, request
import json

app_registro = Blueprint('registro_usuario', __name__, template_folder='templates/registro/', url_prefix='/usuario')

def gravar_registro_usuario(usuario, senha):
    usuarios = []

    with open('usuarios.json', 'r') as arq:
        usuarios = json.load(arq)

    usuarios.append({"usuario": usuario,"senha": senha})

    usuarios_json = json.dumps(usuarios)
    with open('usuarios.json', 'w') as arq:
        arq.write(usuarios_json)

@app_registro.route('/form_registro')
def registro():
    return render_template('registro.html')

@app_registro.route('/registrar_usuario', methods=['Post'])
def registrar():

    if request.method == "POST":
        usuario = request.form['usuario']
        senha = request.form['senha']

        gravar_registro_usuario(usuario, senha)
    return render_template('registro.html')