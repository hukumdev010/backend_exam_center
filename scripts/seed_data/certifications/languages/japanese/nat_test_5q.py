"""NAT-TEST 5Q - Basic Japanese ability test equivalent to JLPT N5"""

CERTIFICATION = {
    "name": "NAT-TEST 5Q",
    "description": "Basic Japanese ability test equivalent to JLPT N5",
    "slug": "nat-test-5q",
    "level": "A1",
    "duration": 105,
    "questions_count": 100,
    "category_slug": "japanese",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "私は学生です。",
        "options": ["I am a student", "I am a teacher", "I am Japanese", "I am fine"],
        "correct_answer": 0,
        "explanation": "私は学生です means 'I am a student'. This is a basic self-introduction pattern."
    },
    {
        "question": "図書館はどこですか。",
        "options": ["Where is the library?", "What is this?", "How are you?", "What time is it?"],
        "correct_answer": 0,
        "explanation": "図書館はどこですか means 'Where is the library?' This asks for location information."
    },
    {
        "question": "毎日七時に起きます。",
        "options": ["I wake up at 7 every day", "I go to bed at 7", "I eat at 7", "I study at 7"],
        "correct_answer": 0,
        "explanation": "毎日七時に起きます means 'I wake up at 7 o'clock every day'. This describes daily routine."
    }
]