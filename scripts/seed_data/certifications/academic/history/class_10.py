"""History Class 10 Certification"""

CERTIFICATION = {
    "name": "History Class 10",
    "description": "Modern history and world events for 10th grade students",
    "slug": "history-class-10",
    "level": "Class 10",
    "duration": 75,
    "questions_count": 30,
    "category_slug": "history",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What caused World War I to begin?",
        "explanation": (
            "The assassination of Archduke Franz Ferdinand of "
            "Austria-Hungary triggered the start of World War I."
        ),
        "reference": "World War I",
        "points": 1,
        "answers": [
            {"text": "Economic crisis", "is_correct": False},
            {"text": "Assassination of Archduke Franz Ferdinand", "is_correct": True},
            {"text": "Colonial disputes", "is_correct": False},
            {"text": "Religious conflicts", "is_correct": False}
        ]
    },
    {
        "text": "Which revolution began in 1789?",
        "explanation": (
            "The French Revolution began in 1789, leading to major "
            "political and social changes in France."
        ),
        "reference": "Revolutions",
        "points": 1,
        "answers": [
            {"text": "American Revolution", "is_correct": False},
            {"text": "Russian Revolution", "is_correct": False},
            {"text": "French Revolution", "is_correct": True},
            {"text": "Industrial Revolution", "is_correct": False}
        ]
    },
    {
        "text": "Who led India's independence movement?",
        "explanation": (
            "Mahatma Gandhi led India's non-violent independence "
            "movement against British colonial rule."
        ),
        "reference": "Independence Movements",
        "points": 1,
        "answers": [
            {"text": "Jawaharlal Nehru", "is_correct": False},
            {"text": "Mahatma Gandhi", "is_correct": True},
            {"text": "Subhas Chandra Bose", "is_correct": False},
            {"text": "Sardar Patel", "is_correct": False}
        ]
    },
    {
        "text": "What was the Cold War?",
        "explanation": (
            "The Cold War was a period of political tension "
            "between the United States and Soviet Union."
        ),
        "reference": "Modern History",
        "points": 1,
        "answers": [
            {"text": "A nuclear war", "is_correct": False},
            {"text": "Political tension between superpowers", "is_correct": True},
            {"text": "A trade war", "is_correct": False},
            {"text": "A civil war", "is_correct": False}
        ]
    },
    {
        "text": "When did the Berlin Wall fall?",
        "explanation": (
            "The Berlin Wall fell in 1989, symbolizing the end "
            "of the Cold War and German reunification."
        ),
        "reference": "Modern History",
        "points": 1,
        "answers": [
            {"text": "1987", "is_correct": False},
            {"text": "1989", "is_correct": True},
            {"text": "1991", "is_correct": False},
            {"text": "1985", "is_correct": False}
        ]
    }
]