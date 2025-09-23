"""HSK Level 2 Certification"""

CERTIFICATION = {
    "name": "HSK Level 2",
    "description": "Elementary Chinese proficiency for 300 common words",
    "slug": "hsk-level-2",
    "level": "A2",
    "duration": 55,
    "questions_count": 12,
    "category_slug": "chinese",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does 现在 (xiànzài) mean?",
        "explanation": "现在 (xiànzài) means 'now' or 'at present', indicating current time.",
        "reference": "HSK Level 2 Time Expressions",
        "points": 1,
        "answers": [
            {"text": "Yesterday", "is_correct": False},
            {"text": "Now", "is_correct": True},
            {"text": "Later", "is_correct": False},
            {"text": "Before", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'because' in Chinese?",
        "explanation": "因为 (yīnwèi) means 'because', used to indicate reason or cause.",
        "reference": "HSK Level 2 Conjunctions",
        "points": 2,
        "answers": [
            {"text": "所以 (suǒyǐ)", "is_correct": False},
            {"text": "因为 (yīnwèi)", "is_correct": True},
            {"text": "但是 (dànshì)", "is_correct": False},
            {"text": "如果 (rúguǒ)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of 工作 (gōngzuò)?",
        "explanation": "工作 (gōngzuò) means 'work' or 'job', both as noun and verb.",
        "reference": "HSK Level 2 Work and Career",
        "points": 1,
        "answers": [
            {"text": "Study", "is_correct": False},
            {"text": "Work/Job", "is_correct": True},
            {"text": "Rest", "is_correct": False},
            {"text": "Play", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'to like' in Chinese?",
        "explanation": "喜欢 (xǐhuan) means 'to like' or 'to enjoy', expressing preference.",
        "reference": "HSK Level 2 Emotions and Preferences",
        "points": 1,
        "answers": [
            {"text": "爱 (ài)", "is_correct": False},
            {"text": "喜欢 (xǐhuan)", "is_correct": True},
            {"text": "想 (xiǎng)", "is_correct": False},
            {"text": "要 (yào)", "is_correct": False},
        ],
    },
    {
        "text": "What does 帮助 (bāngzhù) mean?",
        "explanation": "帮助 (bāngzhù) means 'to help' or 'help/assistance' as noun.",
        "reference": "HSK Level 2 Actions and Helping",
        "points": 1,
        "answers": [
            {"text": "To teach", "is_correct": False},
            {"text": "To help", "is_correct": True},
            {"text": "To learn", "is_correct": False},
            {"text": "To ask", "is_correct": False},
        ],
    },
    {
        "text": "How do you express 'to be able to' in Chinese?",
        "explanation": "可以 (kěyǐ) means 'can' or 'to be able to', indicating ability or permission.",
        "reference": "HSK Level 2 Modal Verbs",
        "points": 2,
        "answers": [
            {"text": "会 (huì)", "is_correct": False},
            {"text": "可以 (kěyǐ)", "is_correct": True},
            {"text": "能 (néng)", "is_correct": False},
            {"text": "要 (yào)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of 地方 (dìfang)?",
        "explanation": "地方 (dìfang) means 'place' or 'location', referring to any location.",
        "reference": "HSK Level 2 Places and Locations",
        "points": 1,
        "answers": [
            {"text": "Time", "is_correct": False},
            {"text": "Place", "is_correct": True},
            {"text": "Person", "is_correct": False},
            {"text": "Thing", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'white' in Chinese?",
        "explanation": "白 (bái) means white, one of the basic color terms in Chinese.",
        "reference": "HSK Level 2 Colors",
        "points": 1,
        "answers": [
            {"text": "黑 (hēi)", "is_correct": False},
            {"text": "红 (hóng)", "is_correct": False},
            {"text": "白 (bái)", "is_correct": True},
            {"text": "蓝 (lán)", "is_correct": False},
        ],
    },
    {
        "text": "What does 开始 (kāishǐ) mean?",
        "explanation": "开始 (kāishǐ) means 'to start' or 'to begin', indicating the beginning of action.",
        "reference": "HSK Level 2 Time and Action Verbs",
        "points": 1,
        "answers": [
            {"text": "To finish", "is_correct": False},
            {"text": "To continue", "is_correct": False},
            {"text": "To start", "is_correct": True},
            {"text": "To stop", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'fast' in Chinese?",
        "explanation": "快 (kuài) means fast or quick, describing speed or pace.",
        "reference": "HSK Level 2 Speed and Movement",
        "points": 1,
        "answers": [
            {"text": "慢 (màn)", "is_correct": False},
            {"text": "快 (kuài)", "is_correct": True},
            {"text": "早 (zǎo)", "is_correct": False},
            {"text": "晚 (wǎn)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of 问题 (wèntí)?",
        "explanation": "问题 (wèntí) means 'question' or 'problem', used in academic and daily contexts.",
        "reference": "HSK Level 2 Academic and General Vocabulary",
        "points": 1,
        "answers": [
            {"text": "Answer", "is_correct": False},
            {"text": "Question/Problem", "is_correct": True},
            {"text": "Solution", "is_correct": False},
            {"text": "Idea", "is_correct": False},
        ],
    },
    {
        "text": "How do you express 'already' in Chinese?",
        "explanation": "已经 (yǐjīng) means 'already', indicating completed action or state.",
        "reference": "HSK Level 2 Aspect Markers",
        "points": 2,
        "answers": [
            {"text": "还 (hái)", "is_correct": False},
            {"text": "就 (jiù)", "is_correct": False},
            {"text": "已经 (yǐjīng)", "is_correct": True},
            {"text": "正在 (zhèngzài)", "is_correct": False},
        ],
    }
]