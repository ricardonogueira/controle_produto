from blueprints.produtos.gerenciamento_prod import app_prod
from blueprints.autenticacao.autenticacao_usuario import app_auth
from blueprints.registro_usuarios.registrar_usuarios import app_registro

from utils.utils_factory_app import criar_app

app = criar_app()

app.register_blueprint(app_prod)
app.register_blueprint(app_auth)
app.register_blueprint(app_registro)