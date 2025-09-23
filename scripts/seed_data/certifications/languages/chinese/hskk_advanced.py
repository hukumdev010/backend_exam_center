"""HSKK Advanced Speaking Certification"""

CERTIFICATION = {
    "name": "HSKK Advanced",
    "description": "HSK Speaking Test for advanced oral expression skills",
    "slug": "hskk-advanced",
    "level": "C1-C2",
    "duration": 24,
    "questions_count": 3,
    "category_slug": "chinese",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Analyze the relationship between technology and society.",
        "explanation": "Provide in-depth analysis of complex social topics with examples.",
        "reference": "HSKK Advanced Social Analysis",
        "points": 4,
        "answers": [
            {"text": "Simple technology list", "is_correct": False},
            {"text": "Complex analysis with multiple perspectives", "is_correct": True},
            {"text": "Personal technology usage", "is_correct": False},
            {"text": "Historical timeline only", "is_correct": False},
        ],
    },
    {
        "text": "Discuss environmental protection strategies and policies.",
        "explanation": "Present sophisticated arguments on environmental issues.",
        "reference": "HSKK Advanced Policy Discussion",
        "points": 4,
        "answers": [
            {"text": "Basic recycling tips", "is_correct": False},
            {"text": "Comprehensive policy analysis with solutions", "is_correct": True},
            {"text": "Personal environmental habits", "is_correct": False},
            {"text": "Environmental problems list", "is_correct": False},
        ],
    },
    {
        "text": "Evaluate cultural exchange impacts in globalization.",
        "explanation": "Demonstrate ability to discuss abstract cultural concepts.",
        "reference": "HSKK Advanced Cultural Analysis",
        "points": 4,
        "answers": [
            {"text": "Cultural differences list", "is_correct": False},
            {"text": "Sophisticated evaluation of cultural impacts", "is_correct": True},
            {"text": "Personal cultural experiences", "is_correct": False},
            {"text": "Traditional customs description", "is_correct": False},
        ],
    }
]