"""KBS Korean Level 2 - KBS Korean proficiency test for elementary level"""

CERTIFICATION = {
    "name": "KBS Korean Level 2",
    "description": "KBS Korean proficiency test for elementary level",
    "slug": "kbs-korean-level-2",
    "level": "A2",
    "duration": 90,
    "questions_count": 60,
    "category_slug": "korean",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "오늘 날씨가 좋네요.",
        "options": ["The weather is nice today", "Today is good", "I like today", "It's sunny today"],
        "correct_answer": 0,
        "explanation": "오늘 날씨가 좋네요 means 'The weather is nice today' - commenting on weather."
    },
    {
        "question": "점심 뭐 드셨어요?",
        "options": ["What did you have for lunch?", "Do you like lunch?", "When is lunch?", "Where is lunch?"],
        "correct_answer": 0,
        "explanation": "점심 뭐 드셨어요? asks what someone ate for lunch using honorific past tense."
    },
    {
        "question": "주말에 쇼핑하러 갈 거예요.",
        "options": ["I will go shopping on the weekend", "I like shopping", "Shopping is fun", "Weekend is good"],
        "correct_answer": 0,
        "explanation": "주말에 쇼핑하러 갈 거예요 expresses future plans using -ㄹ 거예요 pattern."
    }
]