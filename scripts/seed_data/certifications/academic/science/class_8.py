"""Science Class 8 Certification"""

CERTIFICATION = {
    "name": "Science Class 8",
    "description": "Advanced middle school science concepts",
    "slug": "science-class-8",
    "level": "Class 8",
    "duration": 100,
    "questions_count": 50,
    "category_slug": "science",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the smallest particle of an element?",
        "explanation": "An atom is the smallest unit of matter that retains the properties of an element.",
        "reference": "Atomic Structure",
        "points": 1,
        "answers": [
            {"text": "Molecule", "is_correct": False},
            {"text": "Atom", "is_correct": True},
            {"text": "Cell", "is_correct": False},
            {"text": "Electron", "is_correct": False}
        ]
    },
    {
        "text": "Which force keeps us on the ground?",
        "explanation": "Gravity is the force that attracts objects toward the center of the Earth.",
        "reference": "Forces and Motion",
        "points": 1,
        "answers": [
            {"text": "Magnetism", "is_correct": False},
            {"text": "Friction", "is_correct": False},
            {"text": "Gravity", "is_correct": True},
            {"text": "Pressure", "is_correct": False}
        ]
    },
    {
        "text": "What gas makes up most of Earth's atmosphere?",
        "explanation": "Nitrogen makes up about 78% of Earth's atmosphere.",
        "reference": "Earth's Atmosphere",
        "points": 1,
        "answers": [
            {"text": "Oxygen", "is_correct": False},
            {"text": "Carbon dioxide", "is_correct": False},
            {"text": "Nitrogen", "is_correct": True},
            {"text": "Hydrogen", "is_correct": False}
        ]
    }
]