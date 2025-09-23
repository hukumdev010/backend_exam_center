"""Physics Class 11 Certification"""

CERTIFICATION = {
    "name": "Physics Class 11",
    "description": "Physics fundamentals for 11th grade students",
    "slug": "physics-class-11",
    "level": "Class 11",
    "duration": 120,
    "questions_count": 50,
    "category_slug": "physics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the SI unit of force?",
        "explanation": "The Newton (N) is the SI unit of force, named after Sir Isaac Newton.",
        "reference": "Units and Measurements",
        "points": 1,
        "answers": [
            {"text": "Joule", "is_correct": False},
            {"text": "Newton", "is_correct": True},
            {"text": "Watt", "is_correct": False},
            {"text": "Pascal", "is_correct": False}
        ]
    },
    {
        "text": "What is Newton's first law of motion also known as?",
        "explanation": "Newton's first law is also called the law of inertia, stating that an object at rest stays at rest unless acted upon by an external force.",
        "reference": "Laws of Motion",
        "points": 1,
        "answers": [
            {"text": "Law of acceleration", "is_correct": False},
            {"text": "Law of inertia", "is_correct": True},
            {"text": "Law of action-reaction", "is_correct": False},
            {"text": "Law of gravitation", "is_correct": False}
        ]
    },
    {
        "text": "What is the formula for kinetic energy?",
        "explanation": "Kinetic energy is given by KE = (1/2)mv², where m is mass and v is velocity.",
        "reference": "Energy and Work",
        "points": 1,
        "answers": [
            {"text": "mv", "is_correct": False},
            {"text": "(1/2)mv²", "is_correct": True},
            {"text": "mgh", "is_correct": False},
            {"text": "mv²", "is_correct": False}
        ]
    }
]