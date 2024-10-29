from flask import Blueprint, request, jsonify
from app import db

prontuario_bp = Blueprint('prontuario', __name__)

# Modelo Prontuário
class Prontuario(db.Model):
    __tablename__ = 'prontuarios'
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, nullable=False)
    historico = db.Column(db.Text, nullable=False)

@prontuario_bp.route('/', methods=['POST'])
def create_prontuario():
    data = request.get_json()
    if not data.get("historico") or not data.get("paciente_id"):
        return jsonify({"error": "Dados de prontuário incompletos"}), 400
    prontuario = Prontuario(paciente_id=data["paciente_id"], historico=data["historico"])
    db.session.add(prontuario)
    db.session.commit()
    return jsonify({"message": "Prontuário criado com sucesso", "data": data}), 201

@prontuario_bp.route('/', methods=['GET'])
def get_all_prontuarios():
    prontuarios = Prontuario.query.all()
    prontuarios_data = [{"id": p.id, "paciente_id": p.paciente_id, "historico": p.historico} for p in prontuarios]
    return jsonify({"data": prontuarios_data})

@prontuario_bp.route('/<int:id>', methods=['GET'])
def get_prontuario(id):
    prontuario = Prontuario.query.get(id)
    if prontuario is None:
        return jsonify({"error": "Prontuário não encontrado"}), 404
    return jsonify({"data": {"id": prontuario.id, "paciente_id": prontuario.paciente_id, "historico": prontuario.historico}})
