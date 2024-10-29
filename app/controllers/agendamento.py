from flask import Blueprint, request, jsonify
from app import db

agendamento_bp = Blueprint('agendamento', __name__)

# Modelo Agendamento
class Agendamento(db.Model):
    __tablename__ = 'agendamentos'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(20), nullable=False)
    hora = db.Column(db.String(5), nullable=False)
    paciente_id = db.Column(db.Integer, nullable=False)

@agendamento_bp.route('/', methods=['POST'])
def create_agendamento():
    data = request.get_json()
    if not data.get("data") or not data.get("hora") or not data.get("paciente_id"):
        return jsonify({"error": "Dados de agendamento incompletos"}), 400
    agendamento = Agendamento(data=data["data"], hora=data["hora"], paciente_id=data["paciente_id"])
    db.session.add(agendamento)
    db.session.commit()
    return jsonify({"message": "Agendamento criado com sucesso", "data": data}), 201

@agendamento_bp.route('/', methods=['GET'])
def get_all_agendamentos():
    agendamentos = Agendamento.query.all()
    agendamentos_data = [{"id": a.id, "data": a.data, "hora": a.hora, "paciente_id": a.paciente_id} for a in agendamentos]
    return jsonify({"data": agendamentos_data})

@agendamento_bp.route('/<int:id>', methods=['GET'])
def get_agendamento(id):
    agendamento = Agendamento.query.get(id)
    if agendamento is None:
        return jsonify({"error": "Agendamento não encontrado"}), 404
    return jsonify({"data": {"id": agendamento.id, "data": agendamento.data, "hora": agendamento.hora, "paciente_id": agendamento.paciente_id}})
