"""Philosophy Introduction Certification"""

CERTIFICATION = {
    "name": "Philosophy Introduction",
    "description": "Basic philosophical concepts and critical thinking",
    "slug": "philosophy-introduction",
    "level": "Introduction",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "philosophy",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is philosophy?",
        "explanation": (
            "Philosophy is the study of fundamental questions about "
            "existence, knowledge, values, reason, and meaning."
        ),
        "reference": "Introduction to Philosophy",
        "points": 1,
        "answers": [
            {"text": "Study of religion only", "is_correct": False},
            {"text": "Study of fundamental questions", "is_correct": True},
            {"text": "Study of science", "is_correct": False},
            {"text": "Study of mathematics", "is_correct": False}
        ]
    },
    {
        "text": "Who is considered the father of Western philosophy?",
        "explanation": (
            "Socrates is often considered the father of Western philosophy "
            "for his method of questioning and ethical focus."
        ),
        "reference": "Ancient Philosophy",
        "points": 1,
        "answers": [
            {"text": "Plato", "is_correct": False},
            {"text": "Aristotle", "is_correct": False},
            {"text": "Socrates", "is_correct": True},
            {"text": "Pythagoras", "is_correct": False}
        ]
    },
    {
        "text": "What is ethics?",
        "explanation": (
            "Ethics is the branch of philosophy that deals with "
            "moral principles and what is right and wrong."
        ),
        "reference": "Moral Philosophy",
        "points": 1,
        "answers": [
            {"text": "Study of knowledge", "is_correct": False},
            {"text": "Study of moral principles", "is_correct": True},
            {"text": "Study of beauty", "is_correct": False},
            {"text": "Study of logic", "is_correct": False}
        ]
    },
    {
        "text": "What is a valid argument in logic?",
        "explanation": (
            "A valid argument is one where if the premises are true, "
            "the conclusion must necessarily be true."
        ),
        "reference": "Logic",
        "points": 1,
        "answers": [
            {"text": "An argument everyone agrees with", "is_correct": False},
            {"text": "An argument with true conclusion from true premises", "is_correct": True},
            {"text": "An argument with many premises", "is_correct": False},
            {"text": "An argument from authority", "is_correct": False}
        ]
    },
    {
        "text": "What is epistemology?",
        "explanation": (
            "Epistemology is the branch of philosophy that studies "
            "the nature of knowledge, belief, and justification."
        ),
        "reference": "Theory of Knowledge",
        "points": 1,
        "answers": [
            {"text": "Study of existence", "is_correct": False},
            {"text": "Study of knowledge", "is_correct": True},
            {"text": "Study of values", "is_correct": False},
            {"text": "Study of language", "is_correct": False}
        ]
    }
]