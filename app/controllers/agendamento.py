from flask import Blueprint, request, jsonify

agendamento_bp = Blueprint('agendamento', __name__)

@agendamento_bp.route('/', methods=['POST'])
def create_agendamento():
    data = request.get_json()
    # Lógica para criar agendamento
    return jsonify({"message": "Agendamento criado com sucesso", "data": data})
