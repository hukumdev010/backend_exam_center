"""DELF A1 Certification"""

CERTIFICATION = {
    "name": "DELF A1",
    "description": "Basic French language skills for simple everyday situations",
    "slug": "delf-a1",
    "level": "A1",
    "duration": 80,
    "questions_count": 35,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does 'Bonjour' mean in English?",
        "explanation": "Bonjour is the most common French greeting meaning 'Good morning' or 'Hello', used formally and informally.",
        "reference": "DELF A1 Basic Greetings",
        "points": 1,
        "answers": [
            {"text": "Good evening", "is_correct": False},
            {"text": "Good morning/Hello", "is_correct": True},
            {"text": "Goodbye", "is_correct": False},
            {"text": "Thank you", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'please' in French?",
        "explanation": "S'il vous plaît is the formal way to say 'please' in French, while 's'il te plaît' is informal.",
        "reference": "DELF A1 Politeness Expressions",
        "points": 1,
        "answers": [
            {"text": "Merci", "is_correct": False},
            {"text": "S'il vous plaît", "is_correct": True},
            {"text": "Excusez-moi", "is_correct": False},
            {"text": "De rien", "is_correct": False},
        ],
    },
    {
        "text": "What level does DELF A1 correspond to in the CEFR framework?",
        "explanation": "DELF A1 corresponds to the basic user level A1 in the Common European Framework of Reference for Languages.",
        "reference": "DELF A1 Level Description",
        "points": 1,
        "answers": [
            {"text": "A1 - Beginner", "is_correct": True},
            {"text": "A2 - Elementary", "is_correct": False},
            {"text": "B1 - Intermediate", "is_correct": False},
            {"text": "B2 - Upper-intermediate", "is_correct": False},
        ],
    }
]