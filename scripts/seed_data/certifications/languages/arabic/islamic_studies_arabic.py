"""Islamic Studies Arabic Certification"""

CERTIFICATION = {
    "name": "Islamic Studies Arabic",
    "description": "Classical Arabic for Islamic studies and religious texts",
    "slug": "islamic-studies-arabic",
    "level": "Intermediate to Advanced",
    "duration": 160,
    "questions_count": 18,
    "category_slug": "arabic",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is علم التفسير (ilm at-tafsir)?",
        "explanation": "علم التفسير is the science of Quranic "
                      "interpretation and exegesis.",
        "reference": "Islamic Sciences",
        "points": 2,
        "answers": [
            {"text": "Science of Hadith", "is_correct": False},
            {"text": "Science of Quranic interpretation", "is_correct": True},
            {"text": "Science of Islamic law", "is_correct": False},
            {"text": "Science of Arabic grammar", "is_correct": False},
        ],
    },
    {
        "text": "What does علم الحديث (ilm al-hadith) study?",
        "explanation": "علم الحديث is the science that studies the "
                      "sayings, actions, and approvals of Prophet Muhammad.",
        "reference": "Hadith Sciences",
        "points": 2,
        "answers": [
            {"text": "Quranic verses", "is_correct": False},
            {"text": "Prophetic traditions and sayings", "is_correct": True},
            {"text": "Islamic law", "is_correct": False},
            {"text": "Arabic poetry", "is_correct": False},
        ],
    },
    {
        "text": "What is الفقه (al-fiqh) in Islamic studies?",
        "explanation": "الفقه refers to Islamic jurisprudence - "
                      "the understanding and application of Islamic law.",
        "reference": "Islamic Jurisprudence",
        "points": 2,
        "answers": [
            {"text": "Islamic theology", "is_correct": False},
            {"text": "Islamic jurisprudence/law", "is_correct": True},
            {"text": "Islamic ethics", "is_correct": False},
            {"text": "Islamic history", "is_correct": False},
        ],
    },
    {
        "text": "What does السيرة النبوية (as-sira an-nabawiyya) refer to?",
        "explanation": "السيرة النبوية refers to the prophetic "
                      "biography - the life story of Prophet Muhammad.",
        "reference": "Prophetic Biography",
        "points": 2,
        "answers": [
            {"text": "Quranic stories", "is_correct": False},
            {"text": "Prophetic biography", "is_correct": True},
            {"text": "Islamic history", "is_correct": False},
            {"text": "Companion stories", "is_correct": False},
        ],
    },
    {
        "text": "What is علم العقيدة (ilm al-aqida)?",
        "explanation": "علم العقيدة is the science of Islamic "
                      "creed and theology, studying beliefs about Allah.",
        "reference": "Islamic Theology",
        "points": 2,
        "answers": [
            {"text": "Science of Islamic law", "is_correct": False},
            {"text": "Science of Islamic creed/theology", "is_correct": True},
            {"text": "Science of Hadith", "is_correct": False},
            {"text": "Science of Arabic", "is_correct": False},
        ],
    },
    {
        "text": "What does أصول الفقه (usul al-fiqh) mean?",
        "explanation": "أصول الفقه means the principles or "
                      "methodology of Islamic jurisprudence.",
        "reference": "Legal Methodology in Islam",
        "points": 2,
        "answers": [
            {"text": "Branches of Islamic law", "is_correct": False},
            {"text": "Principles of Islamic jurisprudence", "is_correct": True},
            {"text": "History of Islamic law", "is_correct": False},
            {"text": "Comparison of legal schools", "is_correct": False},
        ],
    },
    {
        "text": "What is علم التجويد (ilm at-tajwid)?",
        "explanation": "علم التجويد is the science of proper "
                      "Quranic recitation with correct pronunciation.",
        "reference": "Quranic Recitation Sciences",
        "points": 2,
        "answers": [
            {"text": "Science of Quranic interpretation", "is_correct": False},
            {"text": "Science of proper Quranic recitation", "is_correct": True},
            {"text": "Science of Quranic compilation", "is_correct": False},
            {"text": "Science of Quranic translation", "is_correct": False},
        ],
    },
    {
        "text": "What does المذاهب الأربعة (al-madhahib al-arba'a) refer to?",
        "explanation": "المذاهب الأربعة refers to the four major "
                      "schools of Islamic jurisprudence in Sunni Islam.",
        "reference": "Schools of Islamic Law",
        "points": 2,
        "answers": [
            {"text": "Four Caliphs", "is_correct": False},
            {"text": "Four major schools of Islamic law", "is_correct": True},
            {"text": "Four holy books", "is_correct": False},
            {"text": "Four pillars of Islam", "is_correct": False},
        ],
    },
    {
        "text": "What is الإجماع (al-ijma') in Islamic methodology?",
        "explanation": "الإجماع means scholarly consensus - "
                      "agreement among Islamic scholars on a legal matter.",
        "reference": "Sources of Islamic Law",
        "points": 2,
        "answers": [
            {"text": "Personal opinion", "is_correct": False},
            {"text": "Scholarly consensus", "is_correct": True},
            {"text": "Analogical reasoning", "is_correct": False},
            {"text": "Textual evidence", "is_correct": False},
        ],
    },
    {
        "text": "What does القياس (al-qiyas) mean in Islamic jurisprudence?",
        "explanation": "القياس means analogical reasoning - "
                      "deriving rulings by comparing similar cases.",
        "reference": "Islamic Legal Reasoning",
        "points": 2,
        "answers": [
            {"text": "Scholarly consensus", "is_correct": False},
            {"text": "Analogical reasoning", "is_correct": True},
            {"text": "Textual interpretation", "is_correct": False},
            {"text": "Historical precedent", "is_correct": False},
        ],
    },
    {
        "text": "What is علم الكلام (ilm al-kalam)?",
        "explanation": "علم الكلام is Islamic theology or "
                      "scholastic theology, dealing with rational arguments.",
        "reference": "Islamic Philosophical Theology",
        "points": 2,
        "answers": [
            {"text": "Science of speech", "is_correct": False},
            {"text": "Islamic scholastic theology", "is_correct": True},
            {"text": "Science of rhetoric", "is_correct": False},
            {"text": "Science of debate", "is_correct": False},
        ],
    },
    {
        "text": "What does الصحابة (as-sahaba) refer to?",
        "explanation": "الصحابة refers to the companions of "
                      "Prophet Muhammad who met him and believed in him.",
        "reference": "Early Islamic History",
        "points": 1,
        "answers": [
            {"text": "Early scholars", "is_correct": False},
            {"text": "Companions of the Prophet", "is_correct": True},
            {"text": "Angels", "is_correct": False},
            {"text": "Caliphs", "is_correct": False},
        ],
    },
    {
        "text": "What is التابعون (at-tabi'un)?",
        "explanation": "التابعون refers to the generation that "
                      "followed the companions - those who learned from them.",
        "reference": "Early Muslim Generations",
        "points": 2,
        "answers": [
            {"text": "The companions", "is_correct": False},
            {"text": "The generation after the companions", "is_correct": True},
            {"text": "The prophets", "is_correct": False},
            {"text": "The scholars", "is_correct": False},
        ],
    },
    {
        "text": "What does الإسناد (al-isnad) mean in Hadith science?",
        "explanation": "الإسناد refers to the chain of transmission "
                      "of a Hadith, listing all the narrators.",
        "reference": "Hadith Methodology",
        "points": 2,
        "answers": [
            {"text": "The text of Hadith", "is_correct": False},
            {"text": "The chain of transmission", "is_correct": True},
            {"text": "The interpretation", "is_correct": False},
            {"text": "The authenticity", "is_correct": False},
        ],
    },
    {
        "text": "What is المتن (al-matn) in Hadith terminology?",
        "explanation": "المتن refers to the actual text or "
                      "content of a Hadith, as opposed to its chain.",
        "reference": "Hadith Structure",
        "points": 2,
        "answers": [
            {"text": "The chain of narrators", "is_correct": False},
            {"text": "The text/content of Hadith", "is_correct": True},
            {"text": "The source", "is_correct": False},
            {"text": "The commentary", "is_correct": False},
        ],
    },
    {
        "text": "What does الناسخ والمنسوخ (an-nasikh wa al-mansukh) refer to?",
        "explanation": "الناسخ والمنسوخ refers to the concept of "
                      "abrogation in Islamic texts - later verses superseding "
                      "earlier ones.",
        "reference": "Quranic Sciences",
        "points": 2,
        "answers": [
            {"text": "Translation and original", "is_correct": False},
            {"text": "Abrogating and abrogated verses", "is_correct": True},
            {"text": "Clear and ambiguous verses", "is_correct": False},
            {"text": "Early and late revelations", "is_correct": False},
        ],
    },
    {
        "text": "What is الاجتهاد (al-ijtihad) in Islamic scholarship?",
        "explanation": "الاجتهاد means independent reasoning or "
                      "scholarly effort to derive legal rulings.",
        "reference": "Islamic Legal Methodology",
        "points": 2,
        "answers": [
            {"text": "Following precedent", "is_correct": False},
            {"text": "Independent scholarly reasoning", "is_correct": True},
            {"text": "Memorizing texts", "is_correct": False},
            {"text": "Teaching students", "is_correct": False},
        ],
    },
    {
        "text": "What does البدعة (al-bid'a) mean in Islamic terminology?",
        "explanation": "البدعة refers to religious innovation - "
                      "introducing new practices not from Islamic sources.",
        "reference": "Islamic Religious Practice",
        "points": 2,
        "answers": [
            {"text": "Good deed", "is_correct": False},
            {"text": "Religious innovation", "is_correct": True},
            {"text": "Ancient practice", "is_correct": False},
            {"text": "Scholarly opinion", "is_correct": False},
        ],
    }
]