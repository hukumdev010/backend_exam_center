"""Duolingo English Test Certification"""

CERTIFICATION = {
    "name": "Duolingo English Test",
    "description": "Online English proficiency test accepted by universities worldwide",
    "slug": "duolingo-english-test",
    "level": "A2-C1",
    "duration": 60,
    "questions_count": 50,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "How long does the Duolingo English Test take?",
        "explanation": "The Duolingo English Test takes about 1 hour to complete and provides results within 48 hours.",
        "reference": "Duolingo English Test Overview",
        "points": 1,
        "answers": [
            {"text": "30 minutes", "is_correct": False},
            {"text": "1 hour", "is_correct": True},
            {"text": "2 hours", "is_correct": False},
            {"text": "3 hours", "is_correct": False},
        ],
    }
]