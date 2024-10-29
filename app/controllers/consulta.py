from flask import Blueprint, request, jsonify
from app import db

consulta_bp = Blueprint('consulta', __name__)

# Modelo Consulta
class Consulta(db.Model):
    __tablename__ = 'consultas'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(20), nullable=False)
    medico = db.Column(db.String(100), nullable=False)
    paciente_id = db.Column(db.Integer, nullable=False)

@consulta_bp.route('/', methods=['POST'])
def create_consulta():
    data = request.get_json()
    if not data.get("data") or not data.get("medico") or not data.get("paciente_id"):
        return jsonify({"error": "Dados de consulta incompletos"}), 400
    consulta = Consulta(data=data["data"], medico=data["medico"], paciente_id=data["paciente_id"])
    db.session.add(consulta)
    db.session.commit()
    return jsonify({"message": "Consulta criada com sucesso", "data": data}), 201

@consulta_bp.route('/', methods=['GET'])
def get_all_consultas():
    consultas = Consulta.query.all()
    consultas_data = [{"id": c.id, "data": c.data, "medico": c.medico, "paciente_id": c.paciente_id} for c in consultas]
    return jsonify({"data": consultas_data})

@consulta_bp.route('/<int:id>', methods=['GET'])
def get_consulta(id):
    consulta = Consulta.query.get(id)
    if consulta is None:
        return jsonify({"error": "Consulta não encontrada"}), 404
    return jsonify({"data": {"id": consulta.id, "data": consulta.data, "medico": consulta.medico, "paciente_id": consulta.paciente_id}})
