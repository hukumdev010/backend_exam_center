"""History Class 8 Certification"""

CERTIFICATION = {
    "name": "History Class 8",
    "description": "World history and ancient civilizations for 8th grade",
    "slug": "history-class-8",
    "level": "Class 8",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "history",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Who was the first President of the United States?",
        "explanation": (
            "George Washington served as the first President of "
            "the United States from 1789 to 1797."
        ),
        "reference": "American History",
        "points": 1,
        "answers": [
            {"text": "Thomas Jefferson", "is_correct": False},
            {"text": "George Washington", "is_correct": True},
            {"text": "Abraham Lincoln", "is_correct": False},
            {"text": "John Adams", "is_correct": False}
        ]
    },
    {
        "text": "Which ancient civilization built the pyramids?",
        "explanation": (
            "The ancient Egyptians built the pyramids as tombs "
            "for their pharaohs around 4,500 years ago."
        ),
        "reference": "Ancient Civilizations",
        "points": 1,
        "answers": [
            {"text": "Romans", "is_correct": False},
            {"text": "Greeks", "is_correct": False},
            {"text": "Egyptians", "is_correct": True},
            {"text": "Babylonians", "is_correct": False}
        ]
    },
    {
        "text": "In which year did World War II end?",
        "explanation": (
            "World War II ended in 1945 with the surrender of "
            "Japan after atomic bombs were dropped."
        ),
        "reference": "Modern History",
        "points": 1,
        "answers": [
            {"text": "1944", "is_correct": False},
            {"text": "1945", "is_correct": True},
            {"text": "1946", "is_correct": False},
            {"text": "1943", "is_correct": False}
        ]
    },
    {
        "text": "Who was the famous leader of ancient Macedonia?",
        "explanation": (
            "Alexander the Great conquered much of the known world "
            "and created one of the largest empires in history."
        ),
        "reference": "Ancient History",
        "points": 1,
        "answers": [
            {"text": "Julius Caesar", "is_correct": False},
            {"text": "Alexander the Great", "is_correct": True},
            {"text": "Cleopatra", "is_correct": False},
            {"text": "Hannibal", "is_correct": False}
        ]
    },
    {
        "text": "Which empire was ruled by Genghis Khan?",
        "explanation": (
            "Genghis Khan founded and ruled the Mongol Empire, "
            "the largest contiguous empire in history."
        ),
        "reference": "Medieval History",
        "points": 1,
        "answers": [
            {"text": "Roman Empire", "is_correct": False},
            {"text": "Ottoman Empire", "is_correct": False},
            {"text": "Mongol Empire", "is_correct": True},
            {"text": "British Empire", "is_correct": False}
        ]
    }
]