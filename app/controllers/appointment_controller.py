
# Simulated in-memory database for appointments
appointments = []

def create_appointment(patient_id, description, date):
    """Creates a new appointment for a patient."""
    appointment = {
        "id": len(appointments) + 1,
        "patient_id": patient_id,
        "description": description,
        "date": date,
        "status": "pending"
    }
    appointments.append(appointment)
    return {"message": "Appointment created successfully", "appointment": appointment}

def update_appointment_status(appointment_id, new_status):
    """Updates the status of an appointment."""
    for appointment in appointments:
        if appointment["id"] == appointment_id:
            appointment["status"] = new_status
            return {"message": "Appointment status updated", "appointment": appointment}
    return {"error": "Appointment not found"}
