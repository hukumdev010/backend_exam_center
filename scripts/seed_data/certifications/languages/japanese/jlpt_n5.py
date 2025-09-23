"""JLPT N5 - Basic Japanese proficiency for everyday expressions"""

CERTIFICATION = {
    "name": "JLPT N5",
    "description": "Basic Japanese proficiency for everyday expressions",
    "slug": "jlpt-n5",
    "level": "A1",
    "duration": 105,
    "questions_count": 100,
    "category_slug": "japanese",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "これは何ですか。",
        "options": ["ペンです", "元気です", "学生です", "日本人です"],
        "correct_answer": 0,
        "explanation": "これは何ですか means 'What is this?' The correct answer is ペンです (It's a pen)."
    },
    {
        "question": "今何時ですか。",
        "options": ["二時です", "元気です", "学生です", "日本です"],
        "correct_answer": 0,
        "explanation": "今何時ですか means 'What time is it now?' The correct answer is 二時です (It's 2 o'clock)."
    },
    {
        "question": "お名前は何ですか。",
        "options": ["田中です", "元気です", "学校です", "日本語です"],
        "correct_answer": 0,
        "explanation": "お名前は何ですか means 'What is your name?' The correct answer is 田中です (I'm Tanaka)."
    }
]