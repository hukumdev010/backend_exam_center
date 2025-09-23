"""DELF A2 Certification"""

CERTIFICATION = {
    "name": "DELF A2",
    "description": "Elementary French for routine tasks and simple communication",
    "slug": "delf-a2",
    "level": "A2",
    "duration": 100,
    "questions_count": 40,
    "category_slug": "french",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What can you do at DELF A2 level?",
        "explanation": "At A2 level, you can communicate in routine tasks requiring simple exchange of information on familiar topics.",
        "reference": "DELF A2 Level Competencies",
        "points": 1,
        "answers": [
            {"text": "Handle complex discussions", "is_correct": False},
            {"text": "Communicate in routine tasks", "is_correct": True},
            {"text": "Understand implicit meanings", "is_correct": False},
            {"text": "Write academic papers", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'I would like' in French?",
        "explanation": "Je voudrais is the polite way to express 'I would like' in French, commonly used in shops and restaurants.",
        "reference": "DELF A2 Politeness Forms",
        "points": 1,
        "answers": [
            {"text": "Je veux", "is_correct": False},
            {"text": "Je voudrais", "is_correct": True},
            {"text": "J'ai besoin", "is_correct": False},
            {"text": "Je peux", "is_correct": False},
        ],
    }
]