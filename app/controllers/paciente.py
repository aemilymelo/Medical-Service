from flask import Blueprint, request, jsonify

paciente_bp = Blueprint('paciente', __name__)

@paciente_bp.route('/', methods=['POST'])
def create_paciente():
    data = request.get_json()
    # Lógica para criar paciente
    return jsonify({"message": "Paciente criado com sucesso", "data": data})
