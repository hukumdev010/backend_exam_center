"""Nursing Fundamentals Certification"""

CERTIFICATION = {
    "name": "Nursing Fundamentals",
    "description": "Core nursing principles and patient care basics",
    "slug": "nursing-fundamentals",
    "level": "Beginner",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "nursing",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What are the vital signs?",
        "explanation": (
            "Vital signs include temperature, pulse, respiration, "
            "blood pressure, and sometimes oxygen saturation and pain."
        ),
        "reference": "Nursing Assessment",
        "points": 1,
        "answers": [
            {"text": "Height, weight, age", "is_correct": False},
            {"text": "Temperature, pulse, respiration, BP", "is_correct": True},
            {"text": "Blood type, allergies", "is_correct": False},
            {"text": "Mental status only", "is_correct": False}
        ]
    },
    {
        "text": "What is the normal adult heart rate?",
        "explanation": (
            "Normal adult resting heart rate is typically "
            "60-100 beats per minute."
        ),
        "reference": "Vital Signs",
        "points": 1,
        "answers": [
            {"text": "40-60 bpm", "is_correct": False},
            {"text": "60-100 bpm", "is_correct": True},
            {"text": "100-120 bpm", "is_correct": False},
            {"text": "120-140 bpm", "is_correct": False}
        ]
    },
    {
        "text": "What does HIPAA protect?",
        "explanation": (
            "HIPAA protects patient health information privacy "
            "and regulates its use and disclosure."
        ),
        "reference": "Healthcare Law",
        "points": 1,
        "answers": [
            {"text": "Hospital finances", "is_correct": False},
            {"text": "Patient health information", "is_correct": True},
            {"text": "Medical equipment", "is_correct": False},
            {"text": "Staff schedules", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of hand hygiene?",
        "explanation": (
            "Hand hygiene prevents transmission of microorganisms "
            "between patients, staff, and the environment."
        ),
        "reference": "Infection Control",
        "points": 1,
        "answers": [
            {"text": "Personal cleanliness only", "is_correct": False},
            {"text": "Prevent infection transmission", "is_correct": True},
            {"text": "Hospital policy compliance", "is_correct": False},
            {"text": "Skin care maintenance", "is_correct": False}
        ]
    },
    {
        "text": "What is the nursing process?",
        "explanation": (
            "The nursing process consists of Assessment, Diagnosis, "
            "Planning, Implementation, and Evaluation (ADPIE)."
        ),
        "reference": "Nursing Theory",
        "points": 1,
        "answers": [
            {"text": "Medication administration steps", "is_correct": False},
            {"text": "ADPIE: Assessment to Evaluation", "is_correct": True},
            {"text": "Patient admission procedure", "is_correct": False},
            {"text": "Documentation requirements", "is_correct": False}
        ]
    }
]