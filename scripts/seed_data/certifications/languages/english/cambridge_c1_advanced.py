"""Cambridge C1 Advanced (CAE) Certification"""

CERTIFICATION = {
    "name": "Cambridge C1 Advanced (CAE)",
    "description": "Cambridge English Advanced - high-level English qualification for academic and professional success",
    "slug": "cambridge-c1-advanced",
    "level": "C1",
    "duration": 240,
    "questions_count": 130,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What level does Cambridge C1 Advanced test?",
        "explanation": "Cambridge C1 Advanced tests advanced (C1) level English skills for academic and professional success.",
        "reference": "Cambridge C1 Advanced Overview",
        "points": 1,
        "answers": [
            {"text": "B2 level", "is_correct": False},
            {"text": "C1 level", "is_correct": True},
            {"text": "C2 level", "is_correct": False},
            {"text": "B1 level", "is_correct": False},
        ],
    }
]