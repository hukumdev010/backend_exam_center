"""KBS Korean Level 3 - KBS Korean proficiency test for pre-intermediate level"""

CERTIFICATION = {
    "name": "KBS Korean Level 3",
    "description": "KBS Korean proficiency test for pre-intermediate level",
    "slug": "kbs-korean-level-3",
    "level": "B1",
    "duration": 90,
    "questions_count": 60,
    "category_slug": "korean",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "한국어를 공부한 지 얼마나 되었어요?",
        "options": ["How long have you been studying Korean?", "Do you study Korean?", "Why do you study Korean?", "Where do you study Korean?"],
        "correct_answer": 0,
        "explanation": "한 지 얼마나 되었어요? is a pattern asking about duration of ongoing actions."
    },
    {
        "question": "이 음식은 너무 짜서 못 먹겠어요.",
        "options": ["This food is too salty so I can't eat it", "This food is delicious", "I don't like food", "Food is expensive"],
        "correct_answer": 0,
        "explanation": "너무 짜서 못 먹겠어요 expresses inability due to excessive saltiness using -아서/어서 causality."
    },
    {
        "question": "친구와 약속이 있어서 먼저 가봐야겠어요.",
        "options": ["I have an appointment with a friend so I should leave first", "I like my friend", "My friend is nice", "We made plans"],
        "correct_answer": 0,
        "explanation": "약속이 있어서 and -봐야겠어요 express obligation due to having plans."
    }
]