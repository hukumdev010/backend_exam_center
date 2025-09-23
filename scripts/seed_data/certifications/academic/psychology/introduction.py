"""Psychology Introduction Certification"""

CERTIFICATION = {
    "name": "Psychology Introduction",
    "description": "Basic psychology concepts and human behavior",
    "slug": "psychology-introduction",
    "level": "Introduction",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "psychology",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is psychology?",
        "explanation": (
            "Psychology is the scientific study of mind and behavior, "
            "including thoughts, emotions, and actions."
        ),
        "reference": "Introduction to Psychology",
        "points": 1,
        "answers": [
            {"text": "Study of the brain only", "is_correct": False},
            {"text": "Study of mind and behavior", "is_correct": True},
            {"text": "Study of mental illness", "is_correct": False},
            {"text": "Study of personality", "is_correct": False}
        ]
    },
    {
        "text": "Who is considered the father of psychology?",
        "explanation": (
            "Wilhelm Wundt established the first psychology laboratory "
            "in 1879 and is considered the father of psychology."
        ),
        "reference": "History of Psychology",
        "points": 1,
        "answers": [
            {"text": "Sigmund Freud", "is_correct": False},
            {"text": "Wilhelm Wundt", "is_correct": True},
            {"text": "B.F. Skinner", "is_correct": False},
            {"text": "Carl Jung", "is_correct": False}
        ]
    },
    {
        "text": "What are the main parts of Freud's personality theory?",
        "explanation": (
            "Freud's structural model includes the id (instincts), "
            "ego (reality), and superego (morality)."
        ),
        "reference": "Psychoanalytic Theory",
        "points": 1,
        "answers": [
            {"text": "Conscious, unconscious, preconscious", "is_correct": False},
            {"text": "Id, ego, superego", "is_correct": True},
            {"text": "Mind, body, soul", "is_correct": False},
            {"text": "Thoughts, feelings, behaviors", "is_correct": False}
        ]
    },
    {
        "text": "What is classical conditioning?",
        "explanation": (
            "Classical conditioning is learning through association, "
            "where a neutral stimulus becomes conditioned to produce a response."
        ),
        "reference": "Learning Theory",
        "points": 1,
        "answers": [
            {"text": "Learning through rewards", "is_correct": False},
            {"text": "Learning through association", "is_correct": True},
            {"text": "Learning through observation", "is_correct": False},
            {"text": "Learning through punishment", "is_correct": False}
        ]
    },
    {
        "text": "What is short-term memory capacity according to Miller?",
        "explanation": (
            "George Miller found that short-term memory can hold "
            "about 7 (plus or minus 2) items at once."
        ),
        "reference": "Memory and Cognition",
        "points": 1,
        "answers": [
            {"text": "5 ± 2 items", "is_correct": False},
            {"text": "7 ± 2 items", "is_correct": True},
            {"text": "9 ± 2 items", "is_correct": False},
            {"text": "12 ± 2 items", "is_correct": False}
        ]
    }
]