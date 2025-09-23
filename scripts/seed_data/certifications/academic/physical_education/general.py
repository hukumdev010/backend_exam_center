"""Physical Education & Health Certification"""

CERTIFICATION = {
    "name": "Physical Education & Health",
    "description": "Sports, fitness, and health education concepts",
    "slug": "physical-education-health",
    "level": "General",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "physical_education",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the recommended daily exercise for adults?",
        "explanation": (
            "Adults should get at least 150 minutes of moderate "
            "aerobic activity or 75 minutes of vigorous activity per week."
        ),
        "reference": "Fitness Guidelines",
        "points": 1,
        "answers": [
            {"text": "30 minutes per week", "is_correct": False},
            {"text": "150 minutes per week", "is_correct": True},
            {"text": "300 minutes per week", "is_correct": False},
            {"text": "60 minutes per day", "is_correct": False}
        ]
    },
    {
        "text": "What are the main components of physical fitness?",
        "explanation": (
            "The main components are cardiovascular endurance, "
            "muscular strength, flexibility, and body composition."
        ),
        "reference": "Fitness Components",
        "points": 1,
        "answers": [
            {"text": "Speed and agility only", "is_correct": False},
            {"text": "Strength and endurance only", "is_correct": False},
            {"text": "Endurance, strength, flexibility, composition", "is_correct": True},
            {"text": "Balance and coordination only", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of warming up before exercise?",
        "explanation": (
            "Warming up prepares the body for exercise by increasing "
            "heart rate, blood flow, and muscle temperature."
        ),
        "reference": "Exercise Safety",
        "points": 1,
        "answers": [
            {"text": "To lose weight faster", "is_correct": False},
            {"text": "To prepare body for exercise", "is_correct": True},
            {"text": "To build muscle", "is_correct": False},
            {"text": "To improve flexibility only", "is_correct": False}
        ]
    },
    {
        "text": "How many players are on a basketball team on the court?",
        "explanation": (
            "A basketball team has 5 players on the court at any "
            "given time during the game."
        ),
        "reference": "Sports Rules",
        "points": 1,
        "answers": [
            {"text": "4", "is_correct": False},
            {"text": "5", "is_correct": True},
            {"text": "6", "is_correct": False},
            {"text": "11", "is_correct": False}
        ]
    },
    {
        "text": "What does BMI stand for?",
        "explanation": (
            "BMI stands for Body Mass Index, a measure used to "
            "determine if weight is appropriate for height."
        ),
        "reference": "Health Assessment",
        "points": 1,
        "answers": [
            {"text": "Body Muscle Index", "is_correct": False},
            {"text": "Body Mass Index", "is_correct": True},
            {"text": "Basic Metabolic Index", "is_correct": False},
            {"text": "Body Measurement Index", "is_correct": False}
        ]
    }
]