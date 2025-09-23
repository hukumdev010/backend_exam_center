"""TEF Canada Certification"""

CERTIFICATION = {
    "name": "TEF Canada",
    "description": "French evaluation test for Canadian economic immigration",
    "slug": "tef-canada",
    "level": "A1-C2",
    "duration": 210,
    "questions_count": 180,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is TEF Canada specifically designed for?",
        "explanation": "TEF Canada is designed for French language assessment in Canadian economic immigration programs.",
        "reference": "TEF Canada Immigration",
        "points": 1,
        "answers": [
            {"text": "French university studies", "is_correct": False},
            {"text": "Canadian economic immigration", "is_correct": True},
            {"text": "French business certification", "is_correct": False},
            {"text": "Tourism in Canada", "is_correct": False},
        ],
    }
]