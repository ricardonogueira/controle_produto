from flask import Blueprint, render_template, request
from modelos.usuarios import Usuario
from banco_dados.conexao import db

app_registro = Blueprint('registro_usuario', __name__, template_folder='templates', url_prefix='/usuario')

@app_registro.route('/form_registro')
def registro():
    return render_template('registro.html')

@app_registro.route('/registrar_usuario', methods=['Post'])
def registrar():

    if request.method == "POST":
        usuario_form = request.form['usuario']
        senha_form = request.form['senha']

        usuario = Usuario(
            usuario = usuario_form,
            senha = senha_form
        )
        
        db.session.add(usuario)
        db.session.commit()

    return render_template('registro.html')