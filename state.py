from typing import TypedDict

class MedicalState(TypedDict):

    text: str
    report_type: str
    patient_info: dict
    medical_values: dict
    analysis: dict
    explanation: str