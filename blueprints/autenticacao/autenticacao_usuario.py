from flask import Blueprint, render_template, request, redirect, url_for,session, flash
from sqlalchemy.exc import NoResultFound
from banco_dados.conexao import db
from modelos.usuarios import Usuario

app_auth = Blueprint('autenticacao', __name__, template_folder='templates', url_prefix='/auth')

@app_auth.route('/')
def login():
      return render_template('login.html')

@app_auth.route('/autenticar', methods=['Post'])
def autenticar():

    if request.method == "POST":
        usuario_form = request.form['usuario']
        senha_form = request.form['senha']

        try: 
            usuario_db = db.session.execute(db.select(Usuario).filter_by(usuario = usuario_form, senha = senha_form)).scalar_one()
            print(usuario_db)

            if usuario_db:
                session['logado'] = True
                session['usuario'] = usuario_form
                return redirect( url_for('cad_prod.home') )
            
        except NoResultFound:
            flash("Login ou Senha incorretos")

    return redirect( url_for('.login') )

@app_auth.route('/logout')
def logout():
     session.clear()
     return redirect( url_for('.login') )
            
    