"""Psychology Advanced Certification"""

CERTIFICATION = {
    "name": "Psychology Advanced",
    "description": "Advanced psychology covering abnormal and social psychology",
    "slug": "psychology-advanced",
    "level": "Advanced",
    "duration": 75,
    "questions_count": 30,
    "category_slug": "psychology",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the DSM-5?",
        "explanation": (
            "The DSM-5 is the Diagnostic and Statistical Manual "
            "used to classify and diagnose mental disorders."
        ),
        "reference": "Abnormal Psychology",
        "points": 1,
        "answers": [
            {"text": "A psychological test", "is_correct": False},
            {"text": "Manual for mental disorders", "is_correct": True},
            {"text": "Research methodology", "is_correct": False},
            {"text": "Therapy technique", "is_correct": False}
        ]
    },
    {
        "text": "What is social facilitation?",
        "explanation": (
            "Social facilitation is the tendency for people to "
            "perform better on simple tasks when others are present."
        ),
        "reference": "Social Psychology",
        "points": 1,
        "answers": [
            {"text": "Working better alone", "is_correct": False},
            {"text": "Performance improves with others present", "is_correct": True},
            {"text": "Group decision making", "is_correct": False},
            {"text": "Social pressure", "is_correct": False}
        ]
    },
    {
        "text": "What is cognitive dissonance?",
        "explanation": (
            "Cognitive dissonance is the discomfort felt when holding "
            "contradictory beliefs, values, or attitudes simultaneously."
        ),
        "reference": "Social Psychology",
        "points": 1,
        "answers": [
            {"text": "Memory loss", "is_correct": False},
            {"text": "Conflicting thoughts causing discomfort", "is_correct": True},
            {"text": "Learning disability", "is_correct": False},
            {"text": "Attention deficit", "is_correct": False}
        ]
    },
    {
        "text": "What is a phobia?",
        "explanation": (
            "A phobia is an irrational, excessive fear of a specific "
            "object, situation, or activity."
        ),
        "reference": "Anxiety Disorders",
        "points": 1,
        "answers": [
            {"text": "Rational fear response", "is_correct": False},
            {"text": "Irrational excessive fear", "is_correct": True},
            {"text": "Normal anxiety", "is_correct": False},
            {"text": "Mood disorder", "is_correct": False}
        ]
    },
    {
        "text": "What is the bystander effect?",
        "explanation": (
            "The bystander effect is the phenomenon where individuals "
            "are less likely to help when others are present."
        ),
        "reference": "Social Psychology",
        "points": 1,
        "answers": [
            {"text": "Helping more with others present", "is_correct": False},
            {"text": "Less likely to help with others present", "is_correct": True},
            {"text": "Group cooperation", "is_correct": False},
            {"text": "Leadership behavior", "is_correct": False}
        ]
    }
]