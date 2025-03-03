from flask import Blueprint, render_template, request
from utils.utils_registrar import *

app_registro = Blueprint('registro_usuario', __name__, template_folder='templates/registro/', url_prefix='/usuario')

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