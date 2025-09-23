"""Science Class 3 Certification"""

CERTIFICATION = {
    "name": "Science Class 3",
    "description": "Fundamental science concepts for 3rd grade students",
    "slug": "science-class-3",
    "level": "Class 3",
    "duration": 55,
    "questions_count": 30,
    "category_slug": "science",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the process by which plants make their food?",
        "explanation": "Photosynthesis is the process where plants use sunlight, water, and carbon dioxide to make food.",
        "reference": "Plant Biology",
        "points": 1,
        "answers": [
            {"text": "Respiration", "is_correct": False},
            {"text": "Photosynthesis", "is_correct": True},
            {"text": "Digestion", "is_correct": False},
            {"text": "Absorption", "is_correct": False}
        ]
    },
    {
        "text": "Which part of the plant absorbs water from the soil?",
        "explanation": "Roots absorb water and nutrients from the soil for the plant.",
        "reference": "Plant Parts",
        "points": 1,
        "answers": [
            {"text": "Leaves", "is_correct": False},
            {"text": "Stem", "is_correct": False},
            {"text": "Roots", "is_correct": True},
            {"text": "Flowers", "is_correct": False}
        ]
    },
    {
        "text": "What causes day and night?",
        "explanation": "Day and night are caused by Earth's rotation on its axis.",
        "reference": "Earth's Movement",
        "points": 1,
        "answers": [
            {"text": "Earth moving around the Sun", "is_correct": False},
            {"text": "Earth spinning on its axis", "is_correct": True},
            {"text": "Moon going around Earth", "is_correct": False},
            {"text": "Clouds covering the Sun", "is_correct": False}
        ]
    }
]