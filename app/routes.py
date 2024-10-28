

from flask import Blueprint, request, jsonify
from .controllers.patient_controller import register_patient, get_patient
from .controllers.appointment_controller import create_appointment, update_appointment_status
from .controllers.consultation_controller import schedule_consultation, get_consultation, cancel_consultation

main_routes = Blueprint("main", __name__)

@main_routes.route("/patients", methods=["POST"])
def route_register_patient():
    data = request.json
    response = register_patient(data["name"], data["age"], data["contact"])
    return jsonify(response)

@main_routes.route("/patients/<int:patient_id>", methods=["GET"])
def route_get_patient(patient_id):
    response = get_patient(patient_id)
    return jsonify(response)

@main_routes.route("/appointments", methods=["POST"])
def route_create_appointment():
    data = request.json
    response = create_appointment(data["patient_id"], data["description"], data["date"])
    return jsonify(response)

@main_routes.route("/appointments/<int:appointment_id>", methods=["PATCH"])
def route_update_appointment_status(appointment_id):
    new_status = request.json.get("status")
    response = update_appointment_status(appointment_id, new_status)
    return jsonify(response)

@main_routes.route("/consultations", methods=["POST"])
def route_schedule_consultation():
    data = request.json
    response = schedule_consultation(data["patient_id"], data["date"], data["time"], data["doctor"])
    return jsonify(response)

@main_routes.route("/consultations/<int:consultation_id>", methods=["GET"])
def route_get_consultation(consultation_id):
    response = get_consultation(consultation_id)
    return jsonify(response)

@main_routes.route("/consultations/<int:consultation_id>", methods=["DELETE"])
def route_cancel_consultation(consultation_id):
    response = cancel_consultation(consultation_id)
    return jsonify(response)
