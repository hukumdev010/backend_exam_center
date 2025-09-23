"""TOEFL Essentials Certification"""

CERTIFICATION = {
    "name": "TOEFL Essentials",
    "description": "Shorter, more convenient TOEFL test measuring academic and general English skills",
    "slug": "toefl-essentials",
    "level": "A2-C1",
    "duration": 90,
    "questions_count": 100,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "How does TOEFL Essentials differ from TOEFL iBT?",
        "explanation": "TOEFL Essentials is shorter (90 minutes vs 3 hours) and includes both academic and general English content.",
        "reference": "TOEFL Essentials Overview",
        "points": 1,
        "answers": [
            {"text": "It's longer than TOEFL iBT", "is_correct": False},
            {"text": "It's shorter and includes general English", "is_correct": True},
            {"text": "It's only for beginners", "is_correct": False},
            {"text": "It's only academic English", "is_correct": False},
        ],
    }
]