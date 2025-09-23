"""HSKK Intermediate Speaking Certification"""

CERTIFICATION = {
    "name": "HSKK Intermediate",
    "description": "HSK Speaking Test for intermediate conversation abilities",
    "slug": "hskk-intermediate",
    "level": "B1-B2",
    "duration": 21,
    "questions_count": 5,
    "category_slug": "chinese",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "How would you describe your hometown?",
        "explanation": "Describe hometown using location, features, and personal feelings.",
        "reference": "HSKK Intermediate Descriptive Speaking",
        "points": 3,
        "answers": [
            {"text": "Basic location only", "is_correct": False},
            {"text": "Detailed description with features and feelings", "is_correct": True},
            {"text": "Just the name", "is_correct": False},
            {"text": "Population number only", "is_correct": False},
        ],
    },
    {
        "text": "Explain your favorite hobby and why you enjoy it.",
        "explanation": "Express personal interests with reasons and explanations.",
        "reference": "HSKK Intermediate Personal Interests",
        "points": 3,
        "answers": [
            {"text": "Just name the hobby", "is_correct": False},
            {"text": "Explain hobby with reasons and benefits", "is_correct": True},
            {"text": "List multiple hobbies", "is_correct": False},
            {"text": "Compare with others' hobbies", "is_correct": False},
        ],
    },
    {
        "text": "Describe a memorable travel experience.",
        "explanation": "Narrate past experiences with details and personal reflections.",
        "reference": "HSKK Intermediate Narrative Skills",
        "points": 3,
        "answers": [
            {"text": "Brief summary only", "is_correct": False},
            {"text": "Detailed narrative with reflections", "is_correct": True},
            {"text": "List of places visited", "is_correct": False},
            {"text": "Travel costs and logistics", "is_correct": False},
        ],
    },
    {
        "text": "Express your opinion about social media impact.",
        "explanation": "Share viewpoints on contemporary issues with supporting reasons.",
        "reference": "HSKK Intermediate Opinion Expression",
        "points": 3,
        "answers": [
            {"text": "Simple yes or no", "is_correct": False},
            {"text": "Balanced opinion with supporting reasons", "is_correct": True},
            {"text": "Technical explanation only", "is_correct": False},
            {"text": "Personal usage examples only", "is_correct": False},
        ],
    },
    {
        "text": "Discuss future career plans and goals.",
        "explanation": "Talk about aspirations with concrete plans and reasoning.",
        "reference": "HSKK Intermediate Future Planning",
        "points": 3,
        "answers": [
            {"text": "Job title only", "is_correct": False},
            {"text": "Detailed plans with goals and steps", "is_correct": True},
            {"text": "Salary expectations", "is_correct": False},
            {"text": "Company preferences", "is_correct": False},
        ],
    }
]