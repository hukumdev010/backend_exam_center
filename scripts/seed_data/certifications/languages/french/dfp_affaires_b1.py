"""DFP Affaires B1 Certification"""

CERTIFICATION = {
    "name": "DFP Affaires B1",
    "description": "Professional French diploma for business - intermediate level",
    "slug": "dfp-affaires-b1",
    "level": "B1",
    "duration": 195,
    "questions_count": 85,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does DFP focus on?",
        "explanation": "DFP (Diplôme de français professionnel) focuses on professional French language skills for business contexts.",
        "reference": "DFP Professional French",
        "points": 1,
        "answers": [
            {"text": "Academic French", "is_correct": False},
            {"text": "Professional business French", "is_correct": True},
            {"text": "Literary French", "is_correct": False},
            {"text": "Tourism French", "is_correct": False},
        ],
    }
]