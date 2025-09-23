"""TEF Certification"""

CERTIFICATION = {
    "name": "TEF",
    "description": "Test of French language skills for academic and professional purposes",
    "slug": "tef",
    "level": "A1-C2",
    "duration": 150,
    "questions_count": 150,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does TEF stand for?",
        "explanation": "TEF stands for Test d'évaluation de français, a comprehensive French language assessment.",
        "reference": "TEF Overview",
        "points": 1,
        "answers": [
            {"text": "Test d'évaluation de français", "is_correct": True},
            {"text": "Test d'excellence française", "is_correct": False},
            {"text": "Test d'études françaises", "is_correct": False},
            {"text": "Test d'expression française", "is_correct": False},
        ],
    }
]