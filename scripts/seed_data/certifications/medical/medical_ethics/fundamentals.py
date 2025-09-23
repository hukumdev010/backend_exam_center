"""Medical Ethics Fundamentals Certification"""

CERTIFICATION = {
    "name": "Medical Ethics Fundamentals",
    "description": "Core principles of healthcare ethics and bioethics",
    "slug": "medical-ethics-fundamentals",
    "level": "Intermediate",
    "duration": 50,
    "questions_count": 25,
    "category_slug": "medical_ethics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What are the four principles of biomedical ethics?",
        "explanation": (
            "The four principles are autonomy (respect for persons), "
            "beneficence (do good), non-maleficence (do no harm), "
            "and justice (fairness)."
        ),
        "reference": "Principlism in Bioethics",
        "points": 1,
        "answers": [
            {"text": "Autonomy, beneficence, non-maleficence, justice", 
             "is_correct": True},
            {"text": "Honesty, integrity, compassion, respect", 
             "is_correct": False},
            {"text": "Confidentiality, competence, care, consent", 
             "is_correct": False},
            {"text": "Dignity, fairness, truth, responsibility", 
             "is_correct": False}
        ]
    },
    {
        "text": "What is informed consent?",
        "explanation": (
            "Informed consent is a patient's voluntary agreement "
            "to treatment after understanding risks, benefits, "
            "and alternatives."
        ),
        "reference": "Patient Rights",
        "points": 1,
        "answers": [
            {"text": "Doctor's permission to treat", "is_correct": False},
            {"text": "Patient's informed agreement", "is_correct": True},
            {"text": "Hospital's treatment policy", "is_correct": False},
            {"text": "Insurance approval", "is_correct": False}
        ]
    },
    {
        "text": "What is the principle of autonomy?",
        "explanation": (
            "Autonomy is the right of patients to make decisions "
            "about their medical care without coercion."
        ),
        "reference": "Patient Autonomy",
        "points": 1,
        "answers": [
            {"text": "Doctor makes all decisions", "is_correct": False},
            {"text": "Patient's right to self-determination", 
             "is_correct": True},
            {"text": "Hospital policy compliance", "is_correct": False},
            {"text": "Family member decides", "is_correct": False}
        ]
    },
    {
        "text": "What does 'do no harm' mean?",
        "explanation": (
            "'Do no harm' (non-maleficence) means avoiding "
            "treatments that cause more harm than benefit."
        ),
        "reference": "Non-maleficence",
        "points": 1,
        "answers": [
            {"text": "Never treat patients", "is_correct": False},
            {"text": "Avoid causing unnecessary harm", "is_correct": True},
            {"text": "Use only natural remedies", "is_correct": False},
            {"text": "Refuse all risky procedures", "is_correct": False}
        ]
    },
    {
        "text": "What is confidentiality in healthcare?",
        "explanation": (
            "Confidentiality is the duty to protect patient "
            "information and only share it with authorized persons."
        ),
        "reference": "Patient Privacy",
        "points": 1,
        "answers": [
            {"text": "Keeping all information secret forever", 
             "is_correct": False},
            {"text": "Protecting patient information appropriately", 
             "is_correct": True},
            {"text": "Only sharing with family", "is_correct": False},
            {"text": "Recording everything in detail", "is_correct": False}
        ]
    }
]