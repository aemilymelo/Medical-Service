# Simulated in-memory database for patients
patients = []

def register_patient(name, age, contact):
    """Registers a new patient."""
    patient = {
        "id": len(patients) + 1,
        "name": name,
        "age": age,
        "contact": contact
    }
    patients.append(patient)
    return {"message": "Patient registered successfully", "patient": patient}

def get_patient(patient_id):
    """Retrieves a patient by ID."""
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return {"error": "Patient not found"}
