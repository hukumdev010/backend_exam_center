"""Physics Class 12 Certification"""

CERTIFICATION = {
    "name": "Physics Class 12",
    "description": "Advanced physics for 12th grade students",
    "slug": "physics-class-12",
    "level": "Class 12",
    "duration": 150,
    "questions_count": 60,
    "category_slug": "physics",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the speed of light in vacuum?",
        "explanation": "The speed of light in vacuum is approximately 3 × 10⁸ m/s.",
        "reference": "Electromagnetic Waves",
        "points": 1,
        "answers": [
            {"text": "3 × 10⁶ m/s", "is_correct": False},
            {"text": "3 × 10⁸ m/s", "is_correct": True},
            {"text": "3 × 10¹⁰ m/s", "is_correct": False},
            {"text": "3 × 10⁴ m/s", "is_correct": False}
        ]
    },
    {
        "text": "Which principle explains the working of transformers?",
        "explanation": "Transformers work on the principle of electromagnetic induction, as discovered by Faraday.",
        "reference": "Electromagnetic Induction",
        "points": 1,
        "answers": [
            {"text": "Ohm's law", "is_correct": False},
            {"text": "Electromagnetic induction", "is_correct": True},
            {"text": "Conservation of energy", "is_correct": False},
            {"text": "Lenz's law", "is_correct": False}
        ]
    },
    {
        "text": "What is the photoelectric effect?",
        "explanation": "The photoelectric effect is the emission of electrons from a material when light falls on it, explained by Einstein.",
        "reference": "Quantum Physics",
        "points": 1,
        "answers": [
            {"text": "Emission of electrons due to light", "is_correct": True},
            {"text": "Bending of light", "is_correct": False},
            {"text": "Interference of light waves", "is_correct": False},
            {"text": "Reflection of light", "is_correct": False}
        ]
    }
]