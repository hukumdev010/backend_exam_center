"""Goethe-Zertifikat C1 Certification"""

CERTIFICATION = {
    "name": "Goethe-Zertifikat C1",
    "description": "Advanced German for demanding, longer texts and implicit meaning",
    "slug": "goethe-c1",
    "level": "C1",
    "duration": 240,
    "questions_count": 70,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What distinguishes C1 level German proficiency?",
        "explanation": "C1 level demonstrates advanced proficiency with understanding of demanding texts and recognition of implicit meaning.",
        "reference": "Goethe C1 Advanced Level",
        "points": 1,
        "answers": [
            {"text": "Basic communication only", "is_correct": False},
            {"text": "Advanced with implicit meaning understanding", "is_correct": True},
            {"text": "Elementary level skills", "is_correct": False},
            {"text": "Simple text comprehension", "is_correct": False},
        ],
    }
]