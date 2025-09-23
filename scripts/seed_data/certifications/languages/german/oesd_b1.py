"""ÖSD B1 Certification"""

CERTIFICATION = {
    "name": "ÖSD (Österreichisches Sprachdiplom) B1",
    "description": "Austrian German language diploma - intermediate level",
    "slug": "oesd-b1",
    "level": "B1",
    "duration": 135,
    "questions_count": 45,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does ÖSD stand for?",
        "explanation": "ÖSD stands for Österreichisches Sprachdiplom - Austrian Language Diploma.",
        "reference": "ÖSD Austrian German Certification",
        "points": 1,
        "answers": [
            {"text": "Österreichisches Sprachdiplom", "is_correct": True},
            {"text": "Österreichische Sprach Deutsch", "is_correct": False},
            {"text": "Österreich Sprach Diplom", "is_correct": False},
            {"text": "Österreichische Sprach Dokumentation", "is_correct": False},
        ],
    }
]