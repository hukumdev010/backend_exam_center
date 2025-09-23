"""English Class 10 Certification"""

CERTIFICATION = {
    "name": "English Class 10",
    "description": "Advanced English language and literature for 10th grade",
    "slug": "english-class-10",
    "level": "Class 10",
    "duration": 75,
    "questions_count": 30,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the main theme of Shakespeare's Romeo and Juliet?",
        "explanation": (
            "The central theme of Romeo and Juliet is love conquering "
            "all obstacles, even death."
        ),
        "reference": "Literature",
        "points": 1,
        "answers": [
            {"text": "Revenge", "is_correct": False},
            {"text": "Love", "is_correct": True},
            {"text": "War", "is_correct": False},
            {"text": "Friendship", "is_correct": False}
        ]
    },
    {
        "text": "Which figure of speech compares two things using 'like' or 'as'?",
        "explanation": (
            "A simile is a figure of speech that directly compares "
            "two things using 'like' or 'as'."
        ),
        "reference": "Literary Devices",
        "points": 1,
        "answers": [
            {"text": "Metaphor", "is_correct": False},
            {"text": "Simile", "is_correct": True},
            {"text": "Personification", "is_correct": False},
            {"text": "Hyperbole", "is_correct": False}
        ]
    },
    {
        "text": "What is the correct plural form of 'child'?",
        "explanation": (
            "The word 'child' has an irregular plural form: 'children'."
        ),
        "reference": "Grammar",
        "points": 1,
        "answers": [
            {"text": "Childs", "is_correct": False},
            {"text": "Children", "is_correct": True},
            {"text": "Childes", "is_correct": False},
            {"text": "Child", "is_correct": False}
        ]
    },
    {
        "text": "In which tense is the sentence 'I will have finished'?",
        "explanation": (
            "'Will have finished' indicates future perfect tense, "
            "showing completion before a future point."
        ),
        "reference": "Verb Tenses",
        "points": 1,
        "answers": [
            {"text": "Simple future", "is_correct": False},
            {"text": "Present perfect", "is_correct": False},
            {"text": "Future perfect", "is_correct": True},
            {"text": "Past perfect", "is_correct": False}
        ]
    },
    {
        "text": "What is the antonym of 'expand'?",
        "explanation": (
            "Antonyms are words with opposite meanings. "
            "'Contract' is the opposite of 'expand'."
        ),
        "reference": "Vocabulary",
        "points": 1,
        "answers": [
            {"text": "Grow", "is_correct": False},
            {"text": "Increase", "is_correct": False},
            {"text": "Contract", "is_correct": True},
            {"text": "Extend", "is_correct": False}
        ]
    }
]