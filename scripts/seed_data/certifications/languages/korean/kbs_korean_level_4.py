"""KBS Korean Level 4 - KBS Korean proficiency test for intermediate level"""

CERTIFICATION = {
    "name": "KBS Korean Level 4",
    "description": "KBS Korean proficiency test for intermediate level",
    "slug": "kbs-korean-level-4",
    "level": "B2",
    "duration": 90,
    "questions_count": 60,
    "category_slug": "korean",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "이번 프로젝트는 예상보다 훨씬 복잡해서 시간이 더 걸릴 것 같습니다.",
        "options": ["This project is much more complex than expected so it seems it will take more time", "The project is easy", "I like projects", "Time is important"],
        "correct_answer": 0,
        "explanation": "예상보다 훨씬 복잡해서 expresses comparison and causality in complex sentence structure."
    },
    {
        "question": "회의에서 발표할 자료를 준비하느라고 밤늦게까지 일했어요.",
        "options": ["I worked until late at night preparing materials to present in the meeting", "The meeting was good", "I like presentations", "Work is difficult"],
        "correct_answer": 0,
        "explanation": "-느라고 pattern expresses the reason for doing something that resulted in difficulty or inconvenience."
    },
    {
        "question": "한국 문화에 대해 더 자세히 알고 싶어서 한국학과에 지원했습니다.",
        "options": ["I applied to Korean Studies department because I wanted to know more about Korean culture", "Korean culture is interesting", "I study Korean", "University is good"],
        "correct_answer": 0,
        "explanation": "더 자세히 알고 싶어서 expresses desire for deeper knowledge using causality patterns."
    }
]