from flask import Blueprint, request, jsonify
from app import db

atestado_bp = Blueprint('atestado', __name__)

# Modelo Atestado
class Atestado(db.Model):
    __tablename__ = 'atestados'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    paciente_id = db.Column(db.Integer, nullable=False)

@atestado_bp.route('/', methods=['POST'])
def create_atestado():
    data = request.get_json()
    if not data.get("descricao") or not data.get("paciente_id"):
        return jsonify({"error": "Dados de atestado incompletos"}), 400
    atestado = Atestado(descricao=data["descricao"], paciente_id=data["paciente_id"])
    db.session.add(atestado)
    db.session.commit()
    return jsonify({"message": "Atestado criado com sucesso", "data": data}), 201

@atestado_bp.route('/', methods=['GET'])
def get_all_atestados():
    atestados = Atestado.query.all()
    atestados_data = [{"id": a.id, "descricao": a.descricao, "paciente_id": a.paciente_id} for a in atestados]
    return jsonify({"data": atestados_data})

@atestado_bp.route('/<int:id>', methods=['GET'])
def get_atestado(id):
    atestado = Atestado.query.get(id)
    if atestado is None:
        return jsonify({"error": "Atestado não encontrado"}), 404
    return jsonify({"data": {"id": atestado.id, "descricao": atestado.descricao, "paciente_id": atestado.paciente_id}})
