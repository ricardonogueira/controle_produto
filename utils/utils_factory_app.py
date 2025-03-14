from flask import Flask
from banco_dados.conexao import db
from modelos import *
import config

def criar_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
    app.secret_key = config.SECRET_KEY
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    return app