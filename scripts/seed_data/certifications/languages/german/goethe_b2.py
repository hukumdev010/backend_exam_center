"""Goethe-Zertifikat B2 Certification"""

CERTIFICATION = {
    "name": "Goethe-Zertifikat B2",
    "description": "Upper-intermediate German for complex texts and discussions",
    "slug": "goethe-b2",
    "level": "B2",
    "duration": 210,
    "questions_count": 65,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What can you achieve at B2 level German?",
        "explanation": "B2 level enables understanding of complex texts and active participation in discussions on familiar topics.",
        "reference": "Goethe B2 Capabilities",
        "points": 1,
        "answers": [
            {"text": "Only simple conversations", "is_correct": False},
            {"text": "Complex texts and discussions", "is_correct": True},
            {"text": "Basic greetings only", "is_correct": False},
            {"text": "Elementary vocabulary", "is_correct": False},
        ],
    }
]