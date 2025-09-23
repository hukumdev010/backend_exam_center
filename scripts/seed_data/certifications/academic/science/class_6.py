"""Science Class 6 Certification"""

CERTIFICATION = {
    "name": "Science Class 6",
    "description": "Middle school science fundamentals",
    "slug": "science-class-6",
    "level": "Class 6",
    "duration": 90,
    "questions_count": 40,
    "category_slug": "science",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the basic unit of life?",
        "explanation": "The cell is the basic structural and functional unit of all living organisms.",
        "reference": "Cell Biology",
        "points": 1,
        "answers": [
            {"text": "Tissue", "is_correct": False},
            {"text": "Cell", "is_correct": True},
            {"text": "Organ", "is_correct": False},
            {"text": "Atom", "is_correct": False}
        ]
    },
    {
        "text": "Which gas do plants release during photosynthesis?",
        "explanation": "Plants release oxygen as a byproduct of photosynthesis.",
        "reference": "Photosynthesis",
        "points": 1,
        "answers": [
            {"text": "Carbon dioxide", "is_correct": False},
            {"text": "Nitrogen", "is_correct": False},
            {"text": "Oxygen", "is_correct": True},
            {"text": "Hydrogen", "is_correct": False}
        ]
    },
    {
        "text": "What is the center of our solar system?",
        "explanation": "The Sun is at the center of our solar system and all planets orbit around it.",
        "reference": "Solar System",
        "points": 1,
        "answers": [
            {"text": "Earth", "is_correct": False},
            {"text": "Moon", "is_correct": False},
            {"text": "Sun", "is_correct": True},
            {"text": "Jupiter", "is_correct": False}
        ]
    }
]