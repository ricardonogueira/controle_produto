import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "projeto.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_FOLDER = os.path.abspath('blueprints/produtos/static/uploads')

SECRET_KEY = "SEGURANÇA"

EXTENSOES = {'png', 'jpg', 'jpeg'}
