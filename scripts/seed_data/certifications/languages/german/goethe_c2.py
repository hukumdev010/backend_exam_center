"""Goethe-Zertifikat C2 (GDS) Certification"""

CERTIFICATION = {
    "name": "Goethe-Zertifikat C2 (GDS)",
    "description": "Highest level German certificate showing exceptional language ability",
    "slug": "goethe-c2",
    "level": "C2",
    "duration": 315,
    "questions_count": 80,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the highest level German certification from Goethe Institute?",
        "explanation": "Goethe-Zertifikat C2 (GDS) represents mastery level, demonstrating exceptional German language ability.",
        "reference": "Goethe C2 Mastery Level",
        "points": 1,
        "answers": [
            {"text": "Goethe-Zertifikat B2", "is_correct": False},
            {"text": "Goethe-Zertifikat C1", "is_correct": False},
            {"text": "Goethe-Zertifikat C2 (GDS)", "is_correct": True},
            {"text": "Goethe-Zertifikat B1", "is_correct": False},
        ],
    }
]