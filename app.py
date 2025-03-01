from flask import Flask
from gerenciamento_prod import app_prod
import config

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER
app.secret_key = config.SECRET_KEY

app.register_blueprint(app_prod)