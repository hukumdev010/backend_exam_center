"""DCL FLE Certification"""

CERTIFICATION = {
    "name": "DCL FLE",
    "description": "Professional qualification in French as a Foreign Language teaching",
    "slug": "dcl-fle",
    "level": "B2-C2",
    "duration": 150,
    "questions_count": 80,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does DCL FLE qualify you for?",
        "explanation": "DCL FLE qualifies you for teaching French as a Foreign Language professionally.",
        "reference": "DCL FLE Teaching Qualification",
        "points": 1,
        "answers": [
            {"text": "Business French", "is_correct": False},
            {"text": "Teaching French as Foreign Language", "is_correct": True},
            {"text": "Translation services", "is_correct": False},
            {"text": "Tourism guidance", "is_correct": False},
        ],
    }
]