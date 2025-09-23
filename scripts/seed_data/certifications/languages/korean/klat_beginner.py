"""KLAT Beginner - Korean Language Ability Test for basic proficiency"""

CERTIFICATION = {
    "name": "KLAT Beginner",
    "description": "Korean Language Ability Test for basic proficiency",
    "slug": "klat-beginner",
    "level": "A1-A2",
    "duration": 90,
    "questions_count": 60,
    "category_slug": "korean",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "지금 몇 시예요?",
        "options": ["What time is it now?", "What day is it?", "What month is it?", "What year is it?"],
        "correct_answer": 0,
        "explanation": "지금 몇 시예요? means 'What time is it now?' - asking about current time."
    },
    {
        "question": "어제 뭐 했어요?",
        "options": ["What did you do yesterday?", "What will you do tomorrow?", "What are you doing now?", "What do you usually do?"],
        "correct_answer": 0,
        "explanation": "어제 뭐 했어요? asks about past activities using past tense form."
    },
    {
        "question": "한국어를 얼마나 배웠어요?",
        "options": ["How long have you been learning Korean?", "Do you like learning Korean?", "Is Korean difficult?", "Where do you learn Korean?"],
        "correct_answer": 0,
        "explanation": "This asks about the duration of Korean language learning experience."
    }
]