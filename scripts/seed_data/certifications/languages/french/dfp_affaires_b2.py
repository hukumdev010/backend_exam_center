"""DFP Affaires B2 Certification"""

CERTIFICATION = {
    "name": "DFP Affaires B2",
    "description": "Professional French diploma for business - upper-intermediate level",
    "slug": "dfp-affaires-b2",
    "level": "B2",
    "duration": 225,
    "questions_count": 95,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What level is DFP Affaires B2?",
        "explanation": "DFP Affaires B2 tests upper-intermediate level professional French for business communication.",
        "reference": "DFP B2 Business Level",
        "points": 1,
        "answers": [
            {"text": "B1 level", "is_correct": False},
            {"text": "B2 level", "is_correct": True},
            {"text": "C1 level", "is_correct": False},
            {"text": "A2 level", "is_correct": False},
        ],
    }
]