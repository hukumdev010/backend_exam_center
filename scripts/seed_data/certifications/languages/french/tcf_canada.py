"""TCF Canada Certification"""

CERTIFICATION = {
    "name": "TCF Canada",
    "description": "French proficiency test for Canadian immigration procedures",
    "slug": "tcf-canada",
    "level": "A1-C2",
    "duration": 105,
    "questions_count": 95,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is TCF Canada used for?",
        "explanation": "TCF Canada is specifically designed for French proficiency assessment in Canadian immigration procedures.",
        "reference": "TCF Canada Purpose",
        "points": 1,
        "answers": [
            {"text": "French university admission", "is_correct": False},
            {"text": "Canadian immigration procedures", "is_correct": True},
            {"text": "French citizenship", "is_correct": False},
            {"text": "Business certification", "is_correct": False},
        ],
    }
]