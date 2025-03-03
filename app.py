from flask import Flask
from gerenciamento_prod import app_prod
from autenticacao_usuario import app_auth
from registrar_usuarios import app_registro
import config

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
app.secret_key = config.SECRET_KEY

app.register_blueprint(app_prod)
app.register_blueprint(app_auth)
app.register_blueprint(app_registro)