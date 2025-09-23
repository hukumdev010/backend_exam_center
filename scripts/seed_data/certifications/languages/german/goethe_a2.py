"""Goethe-Zertifikat A2 Certification"""

CERTIFICATION = {
    "name": "Goethe-Zertifikat A2",
    "description": "Elementary German certificate for routine communication tasks",
    "slug": "goethe-a2",
    "level": "A2",
    "duration": 90,
    "questions_count": 45,
    "category_slug": "german",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What can you do at A2 level German?",
        "explanation": "At A2 level, you can communicate in routine tasks requiring simple exchange of information on familiar topics.",
        "reference": "Goethe A2 Level Competencies",
        "points": 1,
        "answers": [
            {"text": "Handle complex business discussions", "is_correct": False},
            {"text": "Communicate in routine tasks", "is_correct": True},
            {"text": "Understand academic lectures", "is_correct": False},
            {"text": "Write professional reports", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'I would like' in German?",
        "explanation": "Ich möchte is the polite way to express 'I would like' in German, commonly used in everyday situations.",
        "reference": "Goethe A2 Polite Expressions",
        "points": 1,
        "answers": [
            {"text": "Ich will", "is_correct": False},
            {"text": "Ich möchte", "is_correct": True},
            {"text": "Ich brauche", "is_correct": False},
            {"text": "Ich kann", "is_correct": False},
        ],
    }
]