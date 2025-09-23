"""TEFAQ Quebec Certification"""

CERTIFICATION = {
    "name": "TEFAQ (Québec)",
    "description": "French evaluation test adapted to Quebec for immigration",
    "slug": "tefaq",
    "level": "A1-C2",
    "duration": 120,
    "questions_count": 100,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is TEFAQ specifically adapted for?",
        "explanation": "TEFAQ is adapted for Quebec French and used for immigration to Quebec province in Canada.",
        "reference": "TEFAQ Quebec Immigration",
        "points": 1,
        "answers": [
            {"text": "France immigration", "is_correct": False},
            {"text": "Quebec immigration", "is_correct": True},
            {"text": "Swiss immigration", "is_correct": False},
            {"text": "Belgian immigration", "is_correct": False},
        ],
    }
]