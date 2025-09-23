"""English Class 9 Certification"""

CERTIFICATION = {
    "name": "English Class 9",
    "description": "English language and literature for 9th grade students",
    "slug": "english-class-9",
    "level": "Class 9",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "english",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Which of the following is a noun?",
        "explanation": (
            "A noun is a word that names a person, place, thing, or idea. "
            "'Happiness' is a noun representing an idea or emotion."
        ),
        "reference": "Parts of Speech",
        "points": 1,
        "answers": [
            {"text": "Run", "is_correct": False},
            {"text": "Beautiful", "is_correct": False},
            {"text": "Happiness", "is_correct": True},
            {"text": "Quickly", "is_correct": False}
        ]
    },
    {
        "text": "What is the past tense of 'go'?",
        "explanation": (
            "The verb 'go' is irregular. Its past tense form is 'went'."
        ),
        "reference": "Verb Tenses",
        "points": 1,
        "answers": [
            {"text": "Goed", "is_correct": False},
            {"text": "Went", "is_correct": True},
            {"text": "Gone", "is_correct": False},
            {"text": "Going", "is_correct": False}
        ]
    },
    {
        "text": "Which punctuation mark ends a question?",
        "explanation": (
            "A question mark (?) is used at the end of interrogative "
            "sentences to indicate a question."
        ),
        "reference": "Punctuation",
        "points": 1,
        "answers": [
            {"text": "Period (.)", "is_correct": False},
            {"text": "Exclamation mark (!)", "is_correct": False},
            {"text": "Question mark (?)", "is_correct": True},
            {"text": "Comma (,)", "is_correct": False}
        ]
    },
    {
        "text": "What is a synonym for 'happy'?",
        "explanation": (
            "Synonyms are words with similar meanings. "
            "'Joyful' has the same meaning as 'happy'."
        ),
        "reference": "Vocabulary",
        "points": 1,
        "answers": [
            {"text": "Sad", "is_correct": False},
            {"text": "Angry", "is_correct": False},
            {"text": "Joyful", "is_correct": True},
            {"text": "Tired", "is_correct": False}
        ]
    },
    {
        "text": "Which is an example of alliteration?",
        "explanation": (
            "Alliteration is the repetition of initial consonant sounds. "
            "'Peter picked peppers' repeats the 'p' sound."
        ),
        "reference": "Literary Devices",
        "points": 1,
        "answers": [
            {"text": "The cat sat", "is_correct": False},
            {"text": "Peter picked peppers", "is_correct": True},
            {"text": "It was raining", "is_correct": False},
            {"text": "She runs fast", "is_correct": False}
        ]
    }
]