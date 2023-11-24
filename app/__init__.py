from flask import Flask
from flask_cors import CORS
from app.controllers.departamento_controller import DepartamentoController
from app.database import db_session, init_db


def create_app():
     app = Flask(__name__)
     CORS(app)

     @app.teardown_appcontext
     def encerrar_sessao(expetion=None):
          db_session.remove()

     init_db()

     app.register_blueprint(DepartamentoController.departamento)

     return app