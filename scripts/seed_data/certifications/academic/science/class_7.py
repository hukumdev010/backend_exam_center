"""Science Class 7 Certification"""

CERTIFICATION = {
    "name": "Science Class 7",
    "description": "Intermediate middle school science",
    "slug": "science-class-7",
    "level": "Class 7",
    "duration": 90,
    "questions_count": 45,
    "category_slug": "science",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the process of water changing from liquid to gas called?",
        "explanation": "Evaporation is the process where liquid water changes to water vapor due to heat.",
        "reference": "Water Cycle",
        "points": 1,
        "answers": [
            {"text": "Condensation", "is_correct": False},
            {"text": "Evaporation", "is_correct": True},
            {"text": "Precipitation", "is_correct": False},
            {"text": "Sublimation", "is_correct": False}
        ]
    },
    {
        "text": "Which organ in the human body pumps blood?",
        "explanation": "The heart is a muscular organ that pumps blood throughout the body.",
        "reference": "Human Circulatory System",
        "points": 1,
        "answers": [
            {"text": "Lungs", "is_correct": False},
            {"text": "Liver", "is_correct": False},
            {"text": "Heart", "is_correct": True},
            {"text": "Kidney", "is_correct": False}
        ]
    },
    {
        "text": "What is the chemical symbol for water?",
        "explanation": "H2O represents water, with 2 hydrogen atoms and 1 oxygen atom.",
        "reference": "Chemical Formulas",
        "points": 1,
        "answers": [
            {"text": "H2O", "is_correct": True},
            {"text": "CO2", "is_correct": False},
            {"text": "NaCl", "is_correct": False},
            {"text": "O2", "is_correct": False}
        ]
    }
]