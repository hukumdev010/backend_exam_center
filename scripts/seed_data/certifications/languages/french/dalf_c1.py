"""DALF C1 Certification"""

CERTIFICATION = {
    "name": "DALF C1",
    "description": "Advanced French for demanding, longer texts and implicit meaning",
    "slug": "dalf-c1",
    "level": "C1",
    "duration": 240,
    "questions_count": 60,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What distinguishes DALF C1 from DELF B2?",
        "explanation": "DALF C1 tests advanced proficiency with understanding of demanding, longer texts and recognition of implicit meaning.",
        "reference": "DALF C1 Advanced Level",
        "points": 1,
        "answers": [
            {"text": "Same level as B2", "is_correct": False},
            {"text": "Advanced with implicit meaning understanding", "is_correct": True},
            {"text": "Only basic communication", "is_correct": False},
            {"text": "Elementary level", "is_correct": False},
        ],
    }
]