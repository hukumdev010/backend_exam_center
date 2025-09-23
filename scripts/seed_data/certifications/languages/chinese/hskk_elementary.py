"""HSKK Elementary Speaking Certification"""

CERTIFICATION = {
    "name": "HSKK Elementary",
    "description": "HSK Speaking Test for basic oral communication skills",
    "slug": "hskk-elementary",
    "level": "A1-A2",
    "duration": 17,
    "questions_count": 8,
    "category_slug": "chinese",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "How would you introduce yourself in Chinese?",
        "explanation": "Basic self-introduction using 我叫... (My name is...)",
        "reference": "HSKK Elementary Self-Introduction",
        "points": 2,
        "answers": [
            {"text": "我叫李明 (Wǒ jiào Lǐ Míng)", "is_correct": True},
            {"text": "你叫什么 (Nǐ jiào shénme)", "is_correct": False},
            {"text": "他是老师 (Tā shì lǎoshī)", "is_correct": False},
            {"text": "这是书 (Zhè shì shū)", "is_correct": False},
        ],
    },
    {
        "text": "How do you ask for someone's age in Chinese?",
        "explanation": "Use 你几岁 for children or 你多大 for general age inquiry.",
        "reference": "HSKK Elementary Age Questions",
        "points": 2,
        "answers": [
            {"text": "你叫什么名字 (Nǐ jiào shénme míngzi)", "is_correct": False},
            {"text": "你多大 (Nǐ duō dà)", "is_correct": True},
            {"text": "你住在哪里 (Nǐ zhù zài nǎlǐ)", "is_correct": False},
            {"text": "你是哪国人 (Nǐ shì nǎ guó rén)", "is_correct": False},
        ],
    },
    {
        "text": "How would you say 'I like Chinese food'?",
        "explanation": "Express preference using 我喜欢... (I like...)",
        "reference": "HSKK Elementary Preferences",
        "points": 2,
        "answers": [
            {"text": "我要中国菜 (Wǒ yào Zhōngguó cài)", "is_correct": False},
            {"text": "我喜欢中国菜 (Wǒ xǐhuan Zhōngguó cài)", "is_correct": True},
            {"text": "我吃中国菜 (Wǒ chī Zhōngguó cài)", "is_correct": False},
            {"text": "我买中国菜 (Wǒ mǎi Zhōngguó cài)", "is_correct": False},
        ],
    },
    {
        "text": "How do you ask about the weather?",
        "explanation": "天气怎么样 is the standard way to ask about weather.",
        "reference": "HSKK Elementary Weather Talk",
        "points": 1,
        "answers": [
            {"text": "今天几月几号 (Jīntiān jǐ yuè jǐ hào)", "is_correct": False},
            {"text": "天气怎么样 (Tiānqì zěnmeyàng)", "is_correct": True},
            {"text": "现在几点 (Xiànzài jǐ diǎn)", "is_correct": False},
            {"text": "今天星期几 (Jīntiān xīngqī jǐ)", "is_correct": False},
        ],
    },
    {
        "text": "How would you ask for directions to a place?",
        "explanation": "Use 去...怎么走 to ask for directions to a place.",
        "reference": "HSKK Elementary Directions",
        "points": 2,
        "answers": [
            {"text": "...在哪里 (...zài nǎlǐ)", "is_correct": False},
            {"text": "去...怎么走 (Qù... zěnme zǒu)", "is_correct": True},
            {"text": "...多远 (...duō yuǎn)", "is_correct": False},
            {"text": "...有什么 (...yǒu shénme)", "is_correct": False},
        ],
    },
    {
        "text": "How do you express that you don't understand?",
        "explanation": "我不懂 or 我不明白 both mean 'I don't understand'.",
        "reference": "HSKK Elementary Communication Problems",
        "points": 1,
        "answers": [
            {"text": "我知道 (Wǒ zhīdào)", "is_correct": False},
            {"text": "我不懂 (Wǒ bù dǒng)", "is_correct": True},
            {"text": "我会说 (Wǒ huì shuō)", "is_correct": False},
            {"text": "我想要 (Wǒ xiǎng yào)", "is_correct": False},
        ],
    },
    {
        "text": "How would you invite someone to eat together?",
        "explanation": "我们一起吃饭吧 means 'Let's eat together'.",
        "reference": "HSKK Elementary Social Invitations",
        "points": 2,
        "answers": [
            {"text": "你吃饭了吗 (Nǐ chīfàn le ma)", "is_correct": False},
            {"text": "我们一起吃饭吧 (Wǒmen yīqǐ chīfàn ba)", "is_correct": True},
            {"text": "我要吃饭 (Wǒ yào chīfàn)", "is_correct": False},
            {"text": "饭很好吃 (Fàn hěn hǎochī)", "is_correct": False},
        ],
    },
    {
        "text": "How do you apologize in Chinese?",
        "explanation": "对不起 is the standard way to say 'sorry' or apologize.",
        "reference": "HSKK Elementary Apologies",
        "points": 1,
        "answers": [
            {"text": "谢谢 (Xièxie)", "is_correct": False},
            {"text": "对不起 (Duìbuqǐ)", "is_correct": True},
            {"text": "不客气 (Bù kèqi)", "is_correct": False},
            {"text": "没关系 (Méi guānxi)", "is_correct": False},
        ],
    }
]