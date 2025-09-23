"""BJT - Business Japanese proficiency for workplace communication"""

CERTIFICATION = {
    "name": "BJT",
    "description": "Business Japanese proficiency for workplace communication",
    "slug": "bjt",
    "level": "B1-C2",
    "duration": 120,
    "questions_count": 100,
    "category_slug": "japanese",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "会議の議事録を作成していただけませんか。",
        "options": ["Could you please create the meeting minutes?", "The meeting is tomorrow", "I don't like meetings", "Minutes are short"],
        "correct_answer": 0,
        "explanation": "This is a polite business request to create meeting minutes using いただけませんか form."
    },
    {
        "question": "売上実績について詳細な分析レポートをお願いします。",
        "options": ["Please provide a detailed analysis report on sales performance", "Sales are good", "I need a report", "Analysis is hard"],
        "correct_answer": 0,
        "explanation": "This is a formal request for detailed sales analysis using business-specific vocabulary."
    },
    {
        "question": "来四半期の予算計画を策定する必要があります。",
        "options": ["We need to formulate the budget plan for next quarter", "Budget is important", "Next quarter is soon", "Planning is difficult"],
        "correct_answer": 0,
        "explanation": "This discusses budget planning using formal business language and 必要があります pattern."
    }
]