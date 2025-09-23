"""Youth Chinese Test (YCT) Level 1 Certification"""

CERTIFICATION = {
    "name": "YCT Level 1",
    "description": "Youth Chinese Test for young learners - Basic level",
    "slug": "yct-level-1",
    "level": "A1",
    "duration": 35,
    "questions_count": 8,
    "category_slug": "chinese",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does 妈妈 (māma) mean?",
        "explanation": "妈妈 means mother, one of the first family words children learn.",
        "reference": "YCT Level 1 Family Members",
        "points": 1,
        "answers": [
            {"text": "Father", "is_correct": False},
            {"text": "Mother", "is_correct": True},
            {"text": "Sister", "is_correct": False},
            {"text": "Grandmother", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'apple' in Chinese?",
        "explanation": "苹果 (píngguǒ) means apple, a common fruit word for children.",
        "reference": "YCT Level 1 Fruits",
        "points": 1,
        "answers": [
            {"text": "香蕉 (xiāngjiāo)", "is_correct": False},
            {"text": "苹果 (píngguǒ)", "is_correct": True},
            {"text": "橙子 (chéngzi)", "is_correct": False},
            {"text": "葡萄 (pútao)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of 红色 (hóngsè)?",
        "explanation": "红色 means red color, basic color vocabulary for young learners.",
        "reference": "YCT Level 1 Colors",
        "points": 1,
        "answers": [
            {"text": "Blue", "is_correct": False},
            {"text": "Red", "is_correct": True},
            {"text": "Yellow", "is_correct": False},
            {"text": "Green", "is_correct": False},
        ],
    },
    {
        "text": "How do you count to three in Chinese?",
        "explanation": "一二三 (yī èr sān) is counting one, two, three in Chinese.",
        "reference": "YCT Level 1 Numbers",
        "points": 1,
        "answers": [
            {"text": "一二三 (yī èr sān)", "is_correct": True},
            {"text": "三二一 (sān èr yī)", "is_correct": False},
            {"text": "二三一 (èr sān yī)", "is_correct": False},
            {"text": "一三二 (yī sān èr)", "is_correct": False},
        ],
    },
    {
        "text": "What does 狗 (gǒu) mean?",
        "explanation": "狗 means dog, a common animal word that children learn early.",
        "reference": "YCT Level 1 Animals",
        "points": 1,
        "answers": [
            {"text": "Cat", "is_correct": False},
            {"text": "Dog", "is_correct": True},
            {"text": "Bird", "is_correct": False},
            {"text": "Fish", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'school' in Chinese?",
        "explanation": "学校 (xuéxiào) means school, important for children's daily life.",
        "reference": "YCT Level 1 Places",
        "points": 1,
        "answers": [
            {"text": "医院 (yīyuàn)", "is_correct": False},
            {"text": "学校 (xuéxiào)", "is_correct": True},
            {"text": "商店 (shāngdiàn)", "is_correct": False},
            {"text": "公园 (gōngyuán)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of 高兴 (gāoxìng)?",
        "explanation": "高兴 means happy or glad, expressing positive emotions.",
        "reference": "YCT Level 1 Emotions",
        "points": 1,
        "answers": [
            {"text": "Sad", "is_correct": False},
            {"text": "Happy", "is_correct": True},
            {"text": "Angry", "is_correct": False},
            {"text": "Tired", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'to play' in Chinese?",
        "explanation": "玩 (wán) means to play, an important verb for children's activities.",
        "reference": "YCT Level 1 Activities",
        "points": 1,
        "answers": [
            {"text": "睡觉 (shuìjiào)", "is_correct": False},
            {"text": "玩 (wán)", "is_correct": True},
            {"text": "学习 (xuéxí)", "is_correct": False},
            {"text": "工作 (gōngzuò)", "is_correct": False},
        ],
    }
]