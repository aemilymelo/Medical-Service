
# Simulated in-memory database for consultations
consultations = []

def schedule_consultation(patient_id, date, time, doctor):
    """Schedules a new consultation for a patient."""
    consultation = {
        "id": len(consultations) + 1,
        "patient_id": patient_id,
        "date": date,
        "time": time,
        "doctor": doctor,
        "status": "scheduled"
    }
    consultations.append(consultation)
    return {"message": "Consultation scheduled successfully", "consultation": consultation}

def get_consultation(consultation_id):
    """Retrieves a consultation by ID."""
    for consultation in consultations:
        if consultation["id"] == consultation_id:
            return consultation
    return {"error": "Consultation not found"}

def cancel_consultation(consultation_id):
    """Cancels a consultation."""
    for consultation in consultations:
        if consultation["id"] == consultation_id:
            consultation["status"] = "canceled"
            return {"message": "Consultation canceled successfully", "consultation": consultation}
    return {"error": "Consultation not found"}
