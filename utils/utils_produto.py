from flask import session, request
from werkzeug.utils import secure_filename
import config, os

def extensoes_permitidas(nome_arquivo):
    return '.' in nome_arquivo and nome_arquivo.rsplit('.', 1)[1].lower() in config.EXTENSOES

def upload_imagem(foto, nome_arquivo="padrao.jpg"):

    if foto.filename != '':
        if foto and extensoes_permitidas(foto.filename):
            nome_arquivo = secure_filename(foto.filename)
            foto.save(os.path.join(config.UPLOAD_FOLDER, nome_arquivo))
            
    return nome_arquivo

def validar_sessao():
    try:
        if session['logado']:
            return True
    except:
        return False
    