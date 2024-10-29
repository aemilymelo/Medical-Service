from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instancia o objeto db do SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical_service.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa o SQLAlchemy com o app
    db.init_app(app)

    # Importa e registra os blueprints
    from app.controllers.agendamento import agendamento_bp
    from app.controllers.atestado import atestado_bp
    from app.controllers.consulta import consulta_bp
    from app.controllers.paciente import paciente_bp
    from app.controllers.prontuario import prontuario_bp
    from app.controllers.medico import medico_bp

    app.register_blueprint(agendamento_bp, url_prefix='/agendamento')
    app.register_blueprint(atestado_bp, url_prefix='/atestado')
    app.register_blueprint(consulta_bp, url_prefix='/consulta')
    app.register_blueprint(paciente_bp, url_prefix='/paciente')
    app.register_blueprint(prontuario_bp, url_prefix='/prontuario')
    app.register_blueprint(medico_bp, url_prefix='/medico')

    # Rota para o caminho raiz
    @app.route('/')
    def home():
        return "Bem-vindo ao Sistema de Atendimento Médico!"

    # Criação das tabelas no banco de dados
    with app.app_context():
        db.create_all()

    return app
