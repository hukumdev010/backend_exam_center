"""EJU Japanese - Japanese proficiency test for university admission"""

CERTIFICATION = {
    "name": "EJU Japanese as Foreign Language",
    "description": "Japanese proficiency test for university admission",
    "slug": "eju-japanese",
    "level": "B2-C1",
    "duration": 125,
    "questions_count": 120,
    "category_slug": "japanese",
    "is_active": True
}

QUESTIONS = [
    {
        "question": "近代化の過程で日本社会が直面した課題について論述しなさい。",
        "options": ["Discuss challenges Japanese society faced during modernization", "Japan is modern", "Society changes", "History is important"],
        "correct_answer": 0,
        "explanation": "This requires academic-level analysis of historical challenges during Japan's modernization."
    },
    {
        "question": "環境問題の解決には国際協力が不可欠である理由を説明せよ。",
        "options": ["Explain why international cooperation is essential for solving environmental problems", "Environment is important", "Countries should work together", "Problems need solutions"],
        "correct_answer": 0,
        "explanation": "This requires academic argumentation about international environmental cooperation."
    },
    {
        "question": "技術革新が社会構造に与える影響を多角的に考察しなさい。",
        "options": ["Examine the impact of technological innovation on social structure from multiple angles", "Technology is advancing", "Society is changing", "Innovation is good"],
        "correct_answer": 0,
        "explanation": "This requires sophisticated academic analysis of technology's societal impact."
    }
]