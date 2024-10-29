# app/controllers/medico.py
from flask import Blueprint, request, jsonify
from app import db

medico_bp = Blueprint('medico', __name__)

# Modelo Médico
class Medico(db.Model):
    __tablename__ = 'medicos'
    idMedico = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(15), unique=True, nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    sexo = db.Column(db.String(50), nullable=True)

@medico_bp.route('/', methods=['POST'])
def create_medico():
    data = request.get_json()
    if not all([data.get("nome"), data.get("cpf"), data.get("especialidade"), data.get("email"), data.get("sexo")]):
        return jsonify({"error": "Dados de médico incompletos"}), 400
    
    medico = Medico(
        nome=data["nome"],
        cpf=data["cpf"],
        especialidade=data["especialidade"],
        email=data["email"],
        sexo=data["sexo"]
    )
    
    db.session.add(medico)
    db.session.commit()
    return jsonify({"message": "Médico criado com sucesso", "data": data}), 201

@medico_bp.route('/', methods=['GET'])
def get_all_medicos():
    medicos = Medico.query.all()
    medicos_data = [
        {
            "idMedico": m.idMedico,
            "nome": m.nome,
            "cpf": m.cpf,
            "especialidade": m.especialidade,
            "email": m.email,
            "sexo": m.sexo
        } for m in medicos
    ]
    return jsonify({"data": medicos_data})

@medico_bp.route('/<int:idMedico>', methods=['GET'])
def get_medico(idMedico):
    medico = Medico.query.get(idMedico)
    if medico is None:
        return jsonify({"error": "Médico não encontrado"}), 404
    return jsonify({"data": {
        "idMedico": medico.idMedico,
        "nome": medico.nome,
        "cpf": medico.cpf,
        "especialidade": medico.especialidade,
        "email": medico.email,
        "sexo": medico.sexo
    }})

@medico_bp.route('/<int:idMedico>', methods=['PUT'])
def update_medico(idMedico):
    medico = Medico.query.get(idMedico)
    if medico is None:
        return jsonify({"error": "Médico não encontrado"}), 404

    data = request.get_json()
    if "nome" in data:
        medico.nome = data["nome"]
    if "cpf" in data:
        medico.cpf = data["cpf"]
    if "especialidade" in data:
        medico.especialidade = data["especialidade"]
    if "email" in data:
        medico.email = data["email"]
    if "sexo" in data:
        medico.sexo = data["sexo"]

    db.session.commit()
    return jsonify({"message": "Médico atualizado com sucesso", "data": {
        "idMedico": medico.idMedico,
        "nome": medico.nome,
        "cpf": medico.cpf,
        "especialidade": medico.especialidade,
        "email": medico.email,
        "sexo": medico.sexo
    }})

@medico_bp.route('/<int:idMedico>', methods=['DELETE'])
def delete_medico(idMedico):
    medico = Medico.query.get(idMedico)
    if medico is None:
        return jsonify({"error": "Médico não encontrado"}), 404

    db.session.delete(medico)
    db.session.commit()
    return jsonify({"message": "Médico deletado com sucesso"}), 204
