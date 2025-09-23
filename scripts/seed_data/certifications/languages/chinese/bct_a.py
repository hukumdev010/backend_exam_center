"""Business Chinese Test (BCT) A Certification"""

CERTIFICATION = {
    "name": "BCT A",
    "description": "Business Chinese Test for basic workplace communication",
    "slug": "bct-a",
    "level": "A2-B1",
    "duration": 105,
    "questions_count": 10,
    "category_slug": "chinese",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does 公司 (gōngsī) mean?",
        "explanation": "公司 means company or corporation in business contexts.",
        "reference": "BCT Business Organizations",
        "points": 1,
        "answers": [
            {"text": "Office", "is_correct": False},
            {"text": "Company", "is_correct": True},
            {"text": "Factory", "is_correct": False},
            {"text": "Store", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'profit' in Chinese?",
        "explanation": "利润 (lìrùn) means profit or earnings in business.",
        "reference": "BCT Financial Terms",
        "points": 2,
        "answers": [
            {"text": "成本 (chéngběn)", "is_correct": False},
            {"text": "利润 (lìrùn)", "is_correct": True},
            {"text": "损失 (sǔnshī)", "is_correct": False},
            {"text": "投资 (tóuzī)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of 市场 (shìchǎng)?",
        "explanation": "市场 means market, either physical marketplace or economic market.",
        "reference": "BCT Market and Trade",
        "points": 1,
        "answers": [
            {"text": "Store", "is_correct": False},
            {"text": "Market", "is_correct": True},
            {"text": "Office", "is_correct": False},
            {"text": "Factory", "is_correct": False},
        ],
    },
    {
        "text": "How do you express 'customer' in Chinese?",
        "explanation": "客户 (kèhù) means customer or client in business contexts.",
        "reference": "BCT Customer Relations",
        "points": 1,
        "answers": [
            {"text": "老板 (lǎobǎn)", "is_correct": False},
            {"text": "客户 (kèhù)", "is_correct": True},
            {"text": "员工 (yuángōng)", "is_correct": False},
            {"text": "经理 (jīnglǐ)", "is_correct": False},
        ],
    },
    {
        "text": "What does 合同 (hétong) mean?",
        "explanation": "合同 means contract or agreement in legal and business contexts.",
        "reference": "BCT Legal Documents",
        "points": 2,
        "answers": [
            {"text": "Report", "is_correct": False},
            {"text": "Contract", "is_correct": True},
            {"text": "Invoice", "is_correct": False},
            {"text": "Receipt", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'to negotiate' in Chinese?",
        "explanation": "谈判 (tánpàn) means to negotiate or hold negotiations.",
        "reference": "BCT Business Communication",
        "points": 2,
        "answers": [
            {"text": "讨论 (tǎolùn)", "is_correct": False},
            {"text": "谈判 (tánpàn)", "is_correct": True},
            {"text": "争论 (zhēnglùn)", "is_correct": False},
            {"text": "商量 (shāngliang)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of 销售 (xiāoshòu)?",
        "explanation": "销售 means sales or to sell products and services.",
        "reference": "BCT Sales and Marketing",
        "points": 1,
        "answers": [
            {"text": "Purchase", "is_correct": False},
            {"text": "Sales", "is_correct": True},
            {"text": "Production", "is_correct": False},
            {"text": "Delivery", "is_correct": False},
        ],
    },
    {
        "text": "How do you express 'budget' in Chinese?",
        "explanation": "预算 (yùsuàn) means budget or financial planning.",
        "reference": "BCT Financial Planning",
        "points": 2,
        "answers": [
            {"text": "账单 (zhàngdān)", "is_correct": False},
            {"text": "预算 (yùsuàn)", "is_correct": True},
            {"text": "收入 (shōurù)", "is_correct": False},
            {"text": "支出 (zhīchū)", "is_correct": False},
        ],
    },
    {
        "text": "What does 效率 (xiàolǜ) mean?",
        "explanation": "效率 means efficiency or effectiveness in work and processes.",
        "reference": "BCT Work Performance",
        "points": 2,
        "answers": [
            {"text": "Quality", "is_correct": False},
            {"text": "Efficiency", "is_correct": True},
            {"text": "Speed", "is_correct": False},
            {"text": "Cost", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'meeting' in Chinese?",
        "explanation": "会议 (huìyì) means meeting or conference in business contexts.",
        "reference": "BCT Business Meetings",
        "points": 1,
        "answers": [
            {"text": "活动 (huódòng)", "is_correct": False},
            {"text": "会议 (huìyì)", "is_correct": True},
            {"text": "聚会 (jùhuì)", "is_correct": False},
            {"text": "访问 (fǎngwèn)", "is_correct": False},
        ],
    }
]