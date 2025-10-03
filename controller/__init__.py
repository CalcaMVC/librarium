# Importa o Flask.
from flask import Flask

# Importa os módulos do back-end.
from . import user_authentication
from . import book_management

# Importa o módulo de banco de dados.
from model.database import Tabular, engine

# Importa a biblioteca para manipulação de diretórios do sistema operacional.
import os

# Função que configura a aplicação da web.
def create_application():

    # Instância da aplicação da web.
    web_application = Flask(__name__, template_folder='../templates', static_folder='../static')

    # Chave de segurança.
    web_application.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mude-isto-no-ambiente')

    # Armazena os cookies com configurações mais seguras (HTTPS).
    web_application.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
    web_application.config['SESSION_COOKIE_SECURE'] = True

    # Mapeia os arquivos de back-end importados.
    web_application.register_blueprint(user_authentication.blueprint)
    web_application.register_blueprint(book_management.blueprint)

    # Cria o banco de dados com o usuário administrador padrão.
    Tabular.metadata.create_all(engine)

    # Retorna a aplicação da web.
    return web_application