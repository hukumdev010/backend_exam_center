"""KBS Korean Level 1 - KBS Korean proficiency test for basic level"""

CERTIFICATION = {
    "name": "KBS Korean Level 1",
    "description": "KBS Korean proficiency test for basic level",
    "slug": "kbs-korean-level-1",
    "level": "A1",
    "duration": 80,
    "questions_count": 50,
    "category_slug": "korean",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "저는 김민수입니다.",
        "options": ["I am Kim Minsu", "My name is teacher", "I am Korean", "I am fine"],
        "correct_answer": 0,
        "explanation": "저는 김민수입니다 means 'I am Kim Minsu' - basic self-introduction pattern."
    },
    {
        "question": "한국어를 배워요.",
        "options": ["I learn Korean", "I speak Korean", "I like Korean", "I am Korean"],
        "correct_answer": 0,
        "explanation": "한국어를 배워요 means 'I learn Korean' using basic present tense form."
    },
    {
        "question": "내일 학교에 가요.",
        "options": ["I go to school tomorrow", "I went to school", "I like school", "School is good"],
        "correct_answer": 0,
        "explanation": "내일 학교에 가요 means 'I go to school tomorrow' expressing future action."
    }
]