"""HSK Level 5 Certification"""

CERTIFICATION = {
    "name": "HSK Level 5",
    "description": "Advanced Chinese proficiency for 2500 common words",
    "slug": "hsk-level-5",
    "level": "C1",
    "duration": 125,
    "questions_count": 6,
    "category_slug": "chinese",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does 概念 (gàiniàn) mean?",
        "explanation": "概念 refers to a concept, notion, or idea.",
        "reference": "HSK Level 5 Abstract Thinking",
        "points": 2,
        "answers": [
            {"text": "Concept", "is_correct": True},
            {"text": "Example", "is_correct": False},
            {"text": "Method", "is_correct": False},
            {"text": "Result", "is_correct": False},
        ],
    },
    {
        "text": "How do you express 'to inherit' in Chinese?",
        "explanation": "继承 (jìchéng) means to inherit or carry on traditions.",
        "reference": "HSK Level 5 Cultural and Legal Terms",
        "points": 2,
        "answers": [
            {"text": "放弃 (fàngqì)", "is_correct": False},
            {"text": "继承 (jìchéng)", "is_correct": True},
            {"text": "创造 (chuàngzào)", "is_correct": False},
            {"text": "改革 (gǎigé)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of 批评 (pīpíng)?",
        "explanation": "批评 means to criticize or critique something.",
        "reference": "HSK Level 5 Evaluation and Judgment",
        "points": 2,
        "answers": [
            {"text": "To praise", "is_correct": False},
            {"text": "To criticize", "is_correct": True},
            {"text": "To ignore", "is_correct": False},
            {"text": "To support", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'conscience' in Chinese?",
        "explanation": "良心 (liángxīn) refers to one's conscience or moral sense.",
        "reference": "HSK Level 5 Moral and Ethical Terms",
        "points": 2,
        "answers": [
            {"text": "理想 (lǐxiǎng)", "is_correct": False},
            {"text": "良心 (liángxīn)", "is_correct": True},
            {"text": "智慧 (zhìhuì)", "is_correct": False},
            {"text": "勇气 (yǒngqì)", "is_correct": False},
        ],
    },
    {
        "text": "What does 贡献 (gòngxiàn) mean?",
        "explanation": "贡献 means contribution or to contribute to something.",
        "reference": "HSK Level 5 Social Contribution",
        "points": 2,
        "answers": [
            {"text": "Sacrifice", "is_correct": False},
            {"text": "Contribution", "is_correct": True},
            {"text": "Achievement", "is_correct": False},
            {"text": "Reward", "is_correct": False},
        ],
    },
    {
        "text": "How do you express 'to rebel' in Chinese?",
        "explanation": "反抗 (fǎnkàng) means to rebel, resist, or oppose authority.",
        "reference": "HSK Level 5 Political and Social Action",
        "points": 2,
        "answers": [
            {"text": "服从 (fúcóng)", "is_correct": False},
            {"text": "反抗 (fǎnkàng)", "is_correct": True},
            {"text": "合作 (hézuò)", "is_correct": False},
            {"text": "支持 (zhīchí)", "is_correct": False},
        ],
    }
]