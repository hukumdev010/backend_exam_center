"""Pathology Fundamentals Certification"""

CERTIFICATION = {
    "name": "Pathology Fundamentals",
    "description": "Basic principles of disease processes and diagnosis",
    "slug": "pathology-fundamentals",
    "level": "Intermediate",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "pathology",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is pathology?",
        "explanation": (
            "Pathology is the study of disease, including its "
            "causes, development, and effects on the body."
        ),
        "reference": "Introduction to Pathology",
        "points": 1,
        "answers": [
            {"text": "Study of normal body function", "is_correct": False},
            {"text": "Study of disease", "is_correct": True},
            {"text": "Study of medications", "is_correct": False},
            {"text": "Study of anatomy", "is_correct": False}
        ]
    },
    {
        "text": "What is inflammation?",
        "explanation": (
            "Inflammation is the body's protective response to "
            "injury, infection, or irritation, characterized by "
            "redness, swelling, heat, pain, and loss of function."
        ),
        "reference": "Inflammatory Response",
        "points": 1,
        "answers": [
            {"text": "Body's response to injury", "is_correct": True},
            {"text": "Normal cell division", "is_correct": False},
            {"text": "Blood clotting process", "is_correct": False},
            {"text": "Nerve signal transmission", "is_correct": False}
        ]
    },
    {
        "text": "What is necrosis?",
        "explanation": (
            "Necrosis is the death of cells or tissues due to "
            "disease, injury, or lack of blood supply."
        ),
        "reference": "Cell Death",
        "points": 1,
        "answers": [
            {"text": "Normal cell aging", "is_correct": False},
            {"text": "Cell or tissue death", "is_correct": True},
            {"text": "Cell multiplication", "is_correct": False},
            {"text": "Cell differentiation", "is_correct": False}
        ]
    },
    {
        "text": "What is a benign tumor?",
        "explanation": (
            "A benign tumor is a non-cancerous growth that "
            "doesn't spread to other parts of the body."
        ),
        "reference": "Tumor Classification",
        "points": 1,
        "answers": [
            {"text": "Cancerous and spreading", "is_correct": False},
            {"text": "Non-cancerous, localized", "is_correct": True},
            {"text": "Infectious growth", "is_correct": False},
            {"text": "Inflammatory lesion", "is_correct": False}
        ]
    },
    {
        "text": "What is metastasis?",
        "explanation": (
            "Metastasis is the spread of cancer cells from the "
            "primary tumor to distant sites in the body."
        ),
        "reference": "Cancer Biology",
        "points": 1,
        "answers": [
            {"text": "Tumor shrinkage", "is_correct": False},
            {"text": "Cancer cell spread", "is_correct": True},
            {"text": "Normal cell growth", "is_correct": False},
            {"text": "Tissue repair", "is_correct": False}
        ]
    }
]