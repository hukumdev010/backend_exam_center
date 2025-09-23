"""telc Deutsch A1 Certification"""

CERTIFICATION = {
    "name": "telc Deutsch A1",
    "description": "Basic German certificate for elementary language skills",
    "slug": "telc-a1",
    "level": "A1",
    "duration": 75,
    "questions_count": 35,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does telc stand for?",
        "explanation": "telc stands for The European Language Certificates, an international language testing organization.",
        "reference": "telc Overview",
        "points": 1,
        "answers": [
            {"text": "The European Language Certificates", "is_correct": True},
            {"text": "Test European Language Center", "is_correct": False},
            {"text": "Total European Language Course", "is_correct": False},
            {"text": "Technical European Language Certificate", "is_correct": False},
        ],
    }
]