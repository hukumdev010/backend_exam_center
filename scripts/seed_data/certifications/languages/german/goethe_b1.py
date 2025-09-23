"""Goethe-Zertifikat B1 Certification"""

CERTIFICATION = {
    "name": "Goethe-Zertifikat B1",
    "description": "Intermediate German for main points of clear standard input",
    "slug": "goethe-b1",
    "level": "B1",
    "duration": 185,
    "questions_count": 50,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What characterizes B1 level German proficiency?",
        "explanation": "B1 level allows you to understand main points of clear standard input on familiar matters and deal with most situations.",
        "reference": "Goethe B1 Competency Framework",
        "points": 1,
        "answers": [
            {"text": "Only basic conversations", "is_correct": False},
            {"text": "Main points of familiar matters", "is_correct": True},
            {"text": "Complex academic texts", "is_correct": False},
            {"text": "Advanced literature", "is_correct": False},
        ],
    }
]