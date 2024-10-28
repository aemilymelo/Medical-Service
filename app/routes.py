from flask import Flask
from app.controllers.agendamento import agendamento_bp
from app.controllers.atestado import atestado_bp
from app.controllers.consulta import consulta_bp
from app.controllers.paciente import paciente_bp
from app.controllers.prontuario import prontuario_bp

def create_app():
    app = Flask(__name__)

    # Registrar blueprints
    app.register_blueprint(agendamento_bp, url_prefix='/agendamento')
    app.register_blueprint(atestado_bp, url_prefix='/atestado')
    app.register_blueprint(consulta_bp, url_prefix='/consulta')
    app.register_blueprint(paciente_bp, url_prefix='/paciente')
    app.register_blueprint(prontuario_bp, url_prefix='/prontuario')

    return app
