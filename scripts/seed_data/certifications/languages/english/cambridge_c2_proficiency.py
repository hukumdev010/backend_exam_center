"""Cambridge C2 Proficiency (CPE) Certification"""

CERTIFICATION = {
    "name": "Cambridge C2 Proficiency (CPE)",
    "description": "Cambridge English Proficiency - highest level English qualification showing exceptional ability",
    "slug": "cambridge-c2-proficiency",
    "level": "C2",
    "duration": 270,
    "questions_count": 150,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the highest level Cambridge English qualification?",
        "explanation": "Cambridge C2 Proficiency is the highest level qualification, demonstrating exceptional English ability at C2 level.",
        "reference": "Cambridge C2 Proficiency Overview",
        "points": 1,
        "answers": [
            {"text": "C1 Advanced", "is_correct": False},
            {"text": "C2 Proficiency", "is_correct": True},
            {"text": "B2 First", "is_correct": False},
            {"text": "B1 Preliminary", "is_correct": False},
        ],
    }
]