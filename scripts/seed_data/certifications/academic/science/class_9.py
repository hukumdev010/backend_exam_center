"""Science Class 9 Certification"""

CERTIFICATION = {
    "name": "Science Class 9",
    "description": "High school science fundamentals",
    "slug": "science-class-9",
    "level": "Class 9",
    "duration": 110,
    "questions_count": 55,
    "category_slug": "science",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the chemical formula for carbon dioxide?",
        "explanation": "CO2 represents carbon dioxide, with 1 carbon atom and 2 oxygen atoms.",
        "reference": "Chemical Compounds",
        "points": 1,
        "answers": [
            {"text": "CO", "is_correct": False},
            {"text": "CO2", "is_correct": True},
            {"text": "C2O", "is_correct": False},
            {"text": "C2O2", "is_correct": False}
        ]
    },
    {
        "text": "Which organelle is known as the powerhouse of the cell?",
        "explanation": "Mitochondria produce ATP, the energy currency of the cell.",
        "reference": "Cell Organelles",
        "points": 1,
        "answers": [
            {"text": "Nucleus", "is_correct": False},
            {"text": "Mitochondria", "is_correct": True},
            {"text": "Ribosome", "is_correct": False},
            {"text": "Chloroplast", "is_correct": False}
        ]
    },
    {
        "text": "What is the speed of light in vacuum?",
        "explanation": "The speed of light in vacuum is approximately 3 x 10^8 meters per second.",
        "reference": "Physics Constants",
        "points": 1,
        "answers": [
            {"text": "3 x 10^8 m/s", "is_correct": True},
            {"text": "3 x 10^6 m/s", "is_correct": False},
            {"text": "3 x 10^10 m/s", "is_correct": False},
            {"text": "3 x 10^7 m/s", "is_correct": False}
        ]
    }
]