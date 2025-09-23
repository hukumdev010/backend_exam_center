"""Business Chinese Test (BCT) B Certification"""

CERTIFICATION = {
    "name": "BCT B",
    "description": "Business Chinese Test for professional business contexts",
    "slug": "bct-b",
    "level": "B2-C1",
    "duration": 135,
    "questions_count": 8,
    "category_slug": "chinese",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does 股份 (gǔfèn) mean in business?",
        "explanation": "股份 means shares or stock ownership in a company.",
        "reference": "BCT Corporate Finance",
        "points": 2,
        "answers": [
            {"text": "Debt", "is_correct": False},
            {"text": "Shares", "is_correct": True},
            {"text": "Assets", "is_correct": False},
            {"text": "Revenue", "is_correct": False},
        ],
    },
    {
        "text": "How do you express 'merger' in Chinese?",
        "explanation": "合并 (hébìng) means merger or consolidation of companies.",
        "reference": "BCT Corporate Strategy",
        "points": 2,
        "answers": [
            {"text": "分离 (fēnlí)", "is_correct": False},
            {"text": "合并 (hébìng)", "is_correct": True},
            {"text": "竞争 (jìngzhēng)", "is_correct": False},
            {"text": "扩张 (kuòzhāng)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of 董事会 (dǒngshìhuì)?",
        "explanation": "董事会 means board of directors in corporate governance.",
        "reference": "BCT Corporate Governance",
        "points": 2,
        "answers": [
            {"text": "Management team", "is_correct": False},
            {"text": "Board of directors", "is_correct": True},
            {"text": "Shareholders", "is_correct": False},
            {"text": "Advisory committee", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'intellectual property' in Chinese?",
        "explanation": "知识产权 (zhīshi chǎnquán) means intellectual property rights.",
        "reference": "BCT Legal and IP Terms",
        "points": 2,
        "answers": [
            {"text": "商标 (shāngbiāo)", "is_correct": False},
            {"text": "知识产权 (zhīshi chǎnquán)", "is_correct": True},
            {"text": "版权 (bǎnquán)", "is_correct": False},
            {"text": "专利 (zhuānlì)", "is_correct": False},
        ],
    },
    {
        "text": "What does 供应链 (gōngyìngliàn) mean?",
        "explanation": "供应链 means supply chain in business logistics.",
        "reference": "BCT Supply Chain Management",
        "points": 2,
        "answers": [
            {"text": "Production line", "is_correct": False},
            {"text": "Supply chain", "is_correct": True},
            {"text": "Distribution network", "is_correct": False},
            {"text": "Retail channel", "is_correct": False},
        ],
    },
    {
        "text": "How do you express 'market share' in Chinese?",
        "explanation": "市场份额 (shìchǎng fèn'é) means market share or market portion.",
        "reference": "BCT Market Analysis",
        "points": 2,
        "answers": [
            {"text": "市场价格 (shìchǎng jiàgé)", "is_correct": False},
            {"text": "市场份额 (shìchǎng fèn'é)", "is_correct": True},
            {"text": "市场需求 (shìchǎng xūqiú)", "is_correct": False},
            {"text": "市场趋势 (shìchǎng qūshì)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of 风险投资 (fēngxiǎn tóuzī)?",
        "explanation": "风险投资 means venture capital or risk investment.",
        "reference": "BCT Investment and Finance",
        "points": 2,
        "answers": [
            {"text": "Bank loan", "is_correct": False},
            {"text": "Venture capital", "is_correct": True},
            {"text": "Government funding", "is_correct": False},
            {"text": "Personal savings", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'corporate culture' in Chinese?",
        "explanation": "企业文化 (qǐyè wénhuà) means corporate or company culture.",
        "reference": "BCT Organizational Behavior",
        "points": 2,
        "answers": [
            {"text": "公司规则 (gōngsī guīzé)", "is_correct": False},
            {"text": "企业文化 (qǐyè wénhuà)", "is_correct": True},
            {"text": "工作环境 (gōngzuò huánjìng)", "is_correct": False},
            {"text": "管理制度 (guǎnlǐ zhìdù)", "is_correct": False},
        ],
    }
]