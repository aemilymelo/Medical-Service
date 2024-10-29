# app/controllers/paciente.py
from flask import Blueprint, request, jsonify
from app import db

paciente_bp = Blueprint('paciente', __name__)

# Modelo Paciente
class Paciente(db.Model):
    __tablename__ = 'pacientes'
    idPaciente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(15), unique=True, nullable=False)
    endereco = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)

@paciente_bp.route('/', methods=['POST'])
def create_paciente():
    data = request.get_json()
    if not all([data.get("nome"), data.get("cpf"), data.get("endereco"), data.get("email")]):
        return jsonify({"error": "Dados de paciente incompletos"}), 400
    
    paciente = Paciente(
        nome=data["nome"],
        cpf=data["cpf"],
        endereco=data["endereco"],
        email=data["email"]
    )
    
    db.session.add(paciente)
    db.session.commit()
    return jsonify({"message": "Paciente criado com sucesso", "data": {
        "idPaciente": paciente.idPaciente,
        "nome": paciente.nome,
        "cpf": paciente.cpf,
        "endereco": paciente.endereco,
        "email": paciente.email
    }}), 201

@paciente_bp.route('/', methods=['GET'])
def get_all_pacientes():
    pacientes = Paciente.query.all()
    pacientes_data = [
        {
            "idPaciente": p.idPaciente,
            "nome": p.nome,
            "cpf": p.cpf,
            "endereco": p.endereco,
            "email": p.email
        } for p in pacientes
    ]
    return jsonify({"data": pacientes_data})

@paciente_bp.route('/<int:idPaciente>', methods=['GET'])
def get_paciente(idPaciente):
    paciente = Paciente.query.get(idPaciente)
    if paciente is None:
        return jsonify({"error": "Paciente não encontrado"}), 404
    return jsonify({"data": {
        "idPaciente": paciente.idPaciente,
        "nome": paciente.nome,
        "cpf": paciente.cpf,
        "endereco": paciente.endereco,
        "email": paciente.email
    }})

@paciente_bp.route('/<int:idPaciente>', methods=['PUT'])
def update_paciente(idPaciente):
    paciente = Paciente.query.get(idPaciente)
    if paciente is None:
        return jsonify({"error": "Paciente não encontrado"}), 404

    data = request.get_json()
    if "nome" in data:
        paciente.nome = data["nome"]
    if "cpf" in data:
        paciente.cpf = data["cpf"]
    if "endereco" in data:
        paciente.endereco = data["endereco"]
    if "email" in data:
        paciente.email = data["email"]

    db.session.commit()
    return jsonify({"message": "Paciente atualizado com sucesso", "data": {
        "idPaciente": paciente.idPaciente,
        "nome": paciente.nome,
        "cpf": paciente.cpf,
        "endereco": paciente.endereco,
        "email": paciente.email
    }})

@paciente_bp.route('/<int:idPaciente>', methods=['DELETE'])
def delete_paciente(idPaciente):
    paciente = Paciente.query.get(idPaciente)
    if paciente is None:
        return jsonify({"error": "Paciente não encontrado"}), 404

    db.session.delete(paciente)
    db.session.commit()
    return jsonify({"message": "Paciente deletado com sucesso"}), 204
