"""Music Theory Certification"""

CERTIFICATION = {
    "name": "Music Theory",
    "description": "Basic music theory and musical concepts",
    "slug": "music-theory",
    "level": "Theory",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "music",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "How many lines does a musical staff have?",
        "explanation": (
            "A musical staff consists of five horizontal lines "
            "on which notes are placed to indicate pitch."
        ),
        "reference": "Music Notation",
        "points": 1,
        "answers": [
            {"text": "4", "is_correct": False},
            {"text": "5", "is_correct": True},
            {"text": "6", "is_correct": False},
            {"text": "7", "is_correct": False}
        ]
    },
    {
        "text": "What are the seven musical notes in Western music?",
        "explanation": (
            "The seven basic musical notes are A, B, C, D, E, F, and G, "
            "which repeat in higher and lower octaves."
        ),
        "reference": "Musical Notes",
        "points": 1,
        "answers": [
            {"text": "A, B, C, D, E, F, G", "is_correct": True},
            {"text": "Do, Re, Mi, Fa, So, La, Ti", "is_correct": False},
            {"text": "1, 2, 3, 4, 5, 6, 7", "is_correct": False},
            {"text": "C, D, E, F, G, A, B", "is_correct": False}
        ]
    },
    {
        "text": "What is tempo in music?",
        "explanation": (
            "Tempo refers to the speed or pace of music, "
            "usually measured in beats per minute (BPM)."
        ),
        "reference": "Musical Elements",
        "points": 1,
        "answers": [
            {"text": "Volume of music", "is_correct": False},
            {"text": "Speed of music", "is_correct": True},
            {"text": "Pitch of music", "is_correct": False},
            {"text": "Style of music", "is_correct": False}
        ]
    },
    {
        "text": "What is a chord?",
        "explanation": (
            "A chord is a combination of three or more different "
            "musical notes played simultaneously."
        ),
        "reference": "Harmony",
        "points": 1,
        "answers": [
            {"text": "Single note", "is_correct": False},
            {"text": "Three or more notes together", "is_correct": True},
            {"text": "Musical rhythm", "is_correct": False},
            {"text": "Loud sound", "is_correct": False}
        ]
    },
    {
        "text": "Who composed 'The Four Seasons'?",
        "explanation": (
            "Antonio Vivaldi composed 'The Four Seasons' in 1723, "
            "a famous set of four violin concertos."
        ),
        "reference": "Classical Music",
        "points": 1,
        "answers": [
            {"text": "Mozart", "is_correct": False},
            {"text": "Bach", "is_correct": False},
            {"text": "Vivaldi", "is_correct": True},
            {"text": "Beethoven", "is_correct": False}
        ]
    }
]