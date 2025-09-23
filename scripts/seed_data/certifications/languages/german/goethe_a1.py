"""Goethe-Zertifikat A1 Certification"""

CERTIFICATION = {
    "name": "Goethe-Zertifikat A1",
    "description": "Basic German language certificate for everyday situations",
    "slug": "goethe-a1",
    "level": "A1",
    "duration": 65,
    "questions_count": 40,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does 'Guten Tag' mean in English?",
        "explanation": "Guten Tag is a common German greeting meaning 'Good day' or 'Hello', used in formal and informal contexts.",
        "reference": "Goethe A1 Basic Greetings",
        "points": 1,
        "answers": [
            {"text": "Good evening", "is_correct": False},
            {"text": "Good day/Hello", "is_correct": True},
            {"text": "Goodbye", "is_correct": False},
            {"text": "Good night", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'please' in German?",
        "explanation": "Bitte is the German word for 'please' and is also used to mean 'you're welcome' or 'here you are'.",
        "reference": "Goethe A1 Politeness",
        "points": 1,
        "answers": [
            {"text": "Danke", "is_correct": False},
            {"text": "Bitte", "is_correct": True},
            {"text": "Entschuldigung", "is_correct": False},
            {"text": "Gern geschehen", "is_correct": False},
        ],
    },
    {
        "text": "What level does Goethe-Zertifikat A1 represent?",
        "explanation": "Goethe-Zertifikat A1 represents beginner level German according to the Common European Framework of Reference.",
        "reference": "Goethe A1 Level Description",
        "points": 1,
        "answers": [
            {"text": "Beginner (A1)", "is_correct": True},
            {"text": "Elementary (A2)", "is_correct": False},
            {"text": "Intermediate (B1)", "is_correct": False},
            {"text": "Advanced (C1)", "is_correct": False},
        ],
    }
]