"""Geography Class 9 Certification"""

CERTIFICATION = {
    "name": "Geography Class 9",
    "description": "Advanced geography covering climate and human geography",
    "slug": "geography-class-9",
    "level": "Class 9",
    "duration": 75,
    "questions_count": 30,
    "category_slug": "geography",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the imaginary line that divides Earth into hemispheres?",
        "explanation": (
            "The equator is an imaginary line at 0° latitude that "
            "divides Earth into Northern and Southern hemispheres."
        ),
        "reference": "Geographic Coordinates",
        "points": 1,
        "answers": [
            {"text": "Prime Meridian", "is_correct": False},
            {"text": "Tropic of Cancer", "is_correct": False},
            {"text": "Equator", "is_correct": True},
            {"text": "International Date Line", "is_correct": False}
        ]
    },
    {
        "text": "Which type of climate is characterized by hot summers and mild winters?",
        "explanation": (
            "Mediterranean climate is characterized by hot, dry summers "
            "and mild, wet winters."
        ),
        "reference": "Climate Types",
        "points": 1,
        "answers": [
            {"text": "Tropical", "is_correct": False},
            {"text": "Mediterranean", "is_correct": True},
            {"text": "Continental", "is_correct": False},
            {"text": "Polar", "is_correct": False}
        ]
    },
    {
        "text": "What is urbanization?",
        "explanation": (
            "Urbanization is the process of people moving from "
            "rural areas to cities, increasing urban population."
        ),
        "reference": "Human Geography",
        "points": 1,
        "answers": [
            {"text": "Building more farms", "is_correct": False},
            {"text": "Movement from cities to villages", "is_correct": False},
            {"text": "Movement from villages to cities", "is_correct": True},
            {"text": "Building more forests", "is_correct": False}
        ]
    },
    {
        "text": "Which ocean is the largest by area?",
        "explanation": (
            "The Pacific Ocean is the largest ocean, covering about "
            "one-third of Earth's surface."
        ),
        "reference": "Physical Geography",
        "points": 1,
        "answers": [
            {"text": "Atlantic Ocean", "is_correct": False},
            {"text": "Indian Ocean", "is_correct": False},
            {"text": "Pacific Ocean", "is_correct": True},
            {"text": "Arctic Ocean", "is_correct": False}
        ]
    },
    {
        "text": "What is the term for the boundary between two tectonic plates?",
        "explanation": (
            "Plate boundaries are where tectonic plates meet, "
            "often causing earthquakes and volcanic activity."
        ),
        "reference": "Earth Science",
        "points": 1,
        "answers": [
            {"text": "Fault line", "is_correct": False},
            {"text": "Plate boundary", "is_correct": True},
            {"text": "Continental shelf", "is_correct": False},
            {"text": "Ocean ridge", "is_correct": False}
        ]
    }
]