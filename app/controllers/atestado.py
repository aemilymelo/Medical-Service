from flask import Blueprint, request, jsonify

atestado_bp = Blueprint('atestado', __name__)

@atestado_bp.route('/', methods=['POST'])
def create_atestado():
    data = request.get_json()
    # Lógica para criar atestado
    return jsonify({"message": "Atestado criado com sucesso", "data": data})
