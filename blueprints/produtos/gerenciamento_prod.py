from flask import Blueprint, render_template, request, redirect, flash, url_for
import config
from utils.utils_produto import *
import os
from modelos.produtos import Produto
from banco_dados.conexao import db

app_prod = Blueprint('cad_prod', __name__, template_folder='templates', static_folder='static', url_prefix='/produtos')

@app_prod.route('/')
def home():

    if validar_sessao():
        lista_produtos = Produto.query.all()
        return render_template('home.html', produtos=lista_produtos)
    
    return redirect( url_for('autenticacao.login') )

@app_prod.route('/adicionar', methods=['GET', 'POST'])
def adicionar():

    if validar_sessao():
        if request.method == "POST":

            if 'foto' in request.files:
                nome_arquivo = upload_imagem(request.files['foto'])            

            produto = Produto( 
                nome=request.form['nome'], 
                preco=float(request.form['preco']),
                quantidade=int(request.form['quantidade']), 
                foto=nome_arquivo
            )

            db.session.add(produto)
            db.session.commit()
            flash("Produto Cadastrado com Sucesso")

            return redirect( url_for('cad_prod.home') )    
        return render_template('adicionar.html')
    
    return redirect( url_for('autenticacao.login') )

@app_prod.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    if validar_sessao():
        produto = Produto.query.get(id)

        if request.method == "POST":

            if 'foto' in request.files:
                nome_arquivo = upload_imagem(request.files['foto'], request.form['imagem'])

            produto.nome = request.form['nome']
            produto.preco = float(request.form['preco'])
            produto.quantidade = int(request.form['quantidade'])
            produto.foto = nome_arquivo
            
            db.session.commit()
            flash("Produto Editado com Sucesso")

            return redirect( url_for('cad_prod.home') )    
        return render_template('editar.html', produto=produto)
    
    return redirect( url_for('autenticacao.login') )

@app_prod.route('/excluir', methods=['POST'])
def excluir():
    
    if validar_sessao():
        indice = int(request.form['id'])
        produto = Produto.query.get(indice)
        db.session.delete(produto)
        db.session.commit()
        flash("Produto Excluído com Sucesso")
        return redirect('/')
    
    return redirect( url_for('autenticacao.login') )