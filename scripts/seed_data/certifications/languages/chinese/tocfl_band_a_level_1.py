"""TOCFL Band A Level 1 Certification"""

CERTIFICATION = {
    "name": "TOCFL Band A Level 1",
    "description": "Taiwan Chinese proficiency test - Novice level",
    "slug": "tocfl-band-a-level-1",
    "level": "A1",
    "duration": 60,
    "questions_count": 8,
    "category_slug": "chinese",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does 台灣 (Táiwān) mean?",
        "explanation": "台灣 means Taiwan, using traditional Chinese characters.",
        "reference": "TOCFL Geography and Places",
        "points": 1,
        "answers": [
            {"text": "China", "is_correct": False},
            {"text": "Taiwan", "is_correct": True},
            {"text": "Japan", "is_correct": False},
            {"text": "Korea", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'traditional characters' in Chinese?",
        "explanation": "繁體字 (fántǐzì) refers to traditional Chinese characters used in Taiwan.",
        "reference": "TOCFL Writing Systems",
        "points": 2,
        "answers": [
            {"text": "简体字 (jiǎntǐzì)", "is_correct": False},
            {"text": "繁體字 (fántǐzì)", "is_correct": True},
            {"text": "漢字 (hànzì)", "is_correct": False},
            {"text": "中文字 (zhōngwénzì)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of 捷運 (jiéyùn)?",
        "explanation": "捷運 means MRT/subway system, commonly used in Taiwan.",
        "reference": "TOCFL Taiwan Transportation",
        "points": 2,
        "answers": [
            {"text": "Bus", "is_correct": False},
            {"text": "MRT/Subway", "is_correct": True},
            {"text": "Taxi", "is_correct": False},
            {"text": "Train", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'night market' in Chinese?",
        "explanation": "夜市 (yèshì) refers to night markets, a famous Taiwan cultural feature.",
        "reference": "TOCFL Taiwan Culture",
        "points": 2,
        "answers": [
            {"text": "商場 (shāngchǎng)", "is_correct": False},
            {"text": "夜市 (yèshì)", "is_correct": True},
            {"text": "超市 (chāoshì)", "is_correct": False},
            {"text": "市場 (shìchǎng)", "is_correct": False},
        ],
    },
    {
        "text": "What does 珍珠奶茶 (zhēnzhū nǎichá) refer to?",
        "explanation": "珍珠奶茶 means bubble tea, originating from Taiwan.",
        "reference": "TOCFL Taiwan Food Culture",
        "points": 1,
        "answers": [
            {"text": "Green tea", "is_correct": False},
            {"text": "Bubble tea", "is_correct": True},
            {"text": "Coffee", "is_correct": False},
            {"text": "Milk", "is_correct": False},
        ],
    },
    {
        "text": "How do you express politeness when asking for help?",
        "explanation": "請問 (qǐngwèn) is a polite way to start questions in Taiwan.",
        "reference": "TOCFL Taiwan Politeness",
        "points": 2,
        "answers": [
            {"text": "你好 (nǐhǎo)", "is_correct": False},
            {"text": "請問 (qǐngwèn)", "is_correct": True},
            {"text": "謝謝 (xièxie)", "is_correct": False},
            {"text": "對不起 (duìbuqǐ)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of 便當 (biàndāng)?",
        "explanation": "便當 means lunch box or bento, common meal format in Taiwan.",
        "reference": "TOCFL Taiwan Dining",
        "points": 1,
        "answers": [
            {"text": "Restaurant", "is_correct": False},
            {"text": "Lunch box", "is_correct": True},
            {"text": "Fast food", "is_correct": False},
            {"text": "Snack", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'convenience store' in Taiwan Chinese?",
        "explanation": "便利商店 (biànlì shāngdiàn) refers to convenience stores like 7-Eleven.",
        "reference": "TOCFL Taiwan Shopping",
        "points": 2,
        "answers": [
            {"text": "超級市場 (chāojí shìchǎng)", "is_correct": False},
            {"text": "便利商店 (biànlì shāngdiàn)", "is_correct": True},
            {"text": "百貨公司 (bǎihuò gōngsī)", "is_correct": False},
            {"text": "專賣店 (zhuānmàidiàn)", "is_correct": False},
        ],
    }
]