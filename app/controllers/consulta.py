from flask import Blueprint, request, jsonify

consulta_bp = Blueprint('consulta', __name__)

@consulta_bp.route('/', methods=['POST'])
def create_consulta():
    data = request.get_json()
    # Lógica para criar consulta
    return jsonify({"message": "Consulta criada com sucesso", "data": data})
