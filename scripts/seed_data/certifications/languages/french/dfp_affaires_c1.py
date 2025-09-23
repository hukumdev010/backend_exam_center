"""DFP Affaires C1 Certification"""

CERTIFICATION = {
    "name": "DFP Affaires C1",
    "description": "Professional French diploma for business - advanced level",
    "slug": "dfp-affaires-c1",
    "level": "C1",
    "duration": 255,
    "questions_count": 105,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the highest level of DFP Affaires?",
        "explanation": "DFP Affaires C1 is the advanced level for professional French in business contexts.",
        "reference": "DFP Advanced Business French",
        "points": 1,
        "answers": [
            {"text": "B2 level", "is_correct": False},
            {"text": "C1 level", "is_correct": True},
            {"text": "C2 level", "is_correct": False},
            {"text": "B1 level", "is_correct": False},
        ],
    }
]