"""Sociology Introduction Certification"""

CERTIFICATION = {
    "name": "Sociology Introduction",
    "description": "Basic sociology concepts and social structures",
    "slug": "sociology-introduction",
    "level": "Introduction",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "sociology",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is sociology?",
        "explanation": (
            "Sociology is the study of society, social relationships, "
            "and human behavior in groups."
        ),
        "reference": "Introduction to Sociology",
        "points": 1,
        "answers": [
            {"text": "Study of individual behavior", "is_correct": False},
            {"text": "Study of society and social behavior", "is_correct": True},
            {"text": "Study of government", "is_correct": False},
            {"text": "Study of economics", "is_correct": False}
        ]
    },
    {
        "text": "Who coined the term 'sociology'?",
        "explanation": (
            "Auguste Comte, a French philosopher, coined the term "
            "'sociology' in the 1830s."
        ),
        "reference": "History of Sociology",
        "points": 1,
        "answers": [
            {"text": "Max Weber", "is_correct": False},
            {"text": "Auguste Comte", "is_correct": True},
            {"text": "Karl Marx", "is_correct": False},
            {"text": "Emile Durkheim", "is_correct": False}
        ]
    },
    {
        "text": "What is socialization?",
        "explanation": (
            "Socialization is the process by which individuals learn "
            "and internalize the values, beliefs, and norms of society."
        ),
        "reference": "Socialization",
        "points": 1,
        "answers": [
            {"text": "Making friends", "is_correct": False},
            {"text": "Learning society's values and norms", "is_correct": True},
            {"text": "Living in groups", "is_correct": False},
            {"text": "Communication skills", "is_correct": False}
        ]
    },
    {
        "text": "What is a social institution?",
        "explanation": (
            "A social institution is an established pattern of behavior "
            "that governs a particular area of social life, like family or education."
        ),
        "reference": "Social Institutions",
        "points": 1,
        "answers": [
            {"text": "A building for social activities", "is_correct": False},
            {"text": "Established patterns governing social life", "is_correct": True},
            {"text": "A government organization", "is_correct": False},
            {"text": "A place of worship", "is_correct": False}
        ]
    },
    {
        "text": "What is social stratification?",
        "explanation": (
            "Social stratification is the hierarchical arrangement "
            "of individuals in society based on wealth, power, and status."
        ),
        "reference": "Social Stratification",
        "points": 1,
        "answers": [
            {"text": "Social organization", "is_correct": False},
            {"text": "Hierarchical arrangement by status", "is_correct": True},
            {"text": "Population distribution", "is_correct": False},
            {"text": "Cultural diversity", "is_correct": False}
        ]
    }
]