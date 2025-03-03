from flask import Blueprint, render_template, request, redirect, url_for,session, flash
import json

app_auth = Blueprint('autenticacao', __name__, template_folder='templates/auth/', url_prefix='/auth')

usuarios = []

def ler_arquivo_json():
    global usuarios
    with open('usuarios.json', 'r') as arq:
            usuarios = json.load(arq)

def escrever_arquivo_json():
     with open('usuarios.json', 'w+') as arq:
            arq.write("[]")

def carregar_usuarios_arquivo():
    global produtos

    try:
        ler_arquivo_json()

    except FileNotFoundError:
        escrever_arquivo_json()
        ler_arquivo_json()

carregar_usuarios_arquivo()

@app_auth.route('/')
def login():
      return render_template('login.html')

@app_auth.route('/autenticar', methods=['Post'])
def autenticar():

    if request.method == "POST":
        usuario_form = request.form['usuario']
        senha_form = request.form['senha']

        for usuario in usuarios:
            if usuario['usuario'] == usuario_form and usuario['senha'] == senha_form:
                print('Dentro IF')
                session['logado'] = True
                session['usuario'] = usuario_form
                return redirect( url_for('cad_prod.home') )

    flash("Login ou Senha incorretos")
    return render_template('login.html')

@app_auth.route('/logout')
def logout():
     session.clear()
     return redirect( url_for('.login') )
            
    