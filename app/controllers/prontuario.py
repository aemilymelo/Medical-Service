from flask import Blueprint, request, jsonify

prontuario_bp = Blueprint('prontuario', __name__)

@prontuario_bp.route('/', methods=['POST'])
def create_prontuario():
    data = request.get_json()
    # Lógica para criar prontuário
    return jsonify({"message": "Prontuário criado com sucesso", "data": data})
