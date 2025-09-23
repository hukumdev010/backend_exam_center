"""Business Arabic Certification"""

CERTIFICATION = {
    "name": "Business Arabic Professional",
    "description": "Arabic language skills for business and commercial contexts",
    "slug": "business-arabic-professional",
    "level": "Intermediate to Advanced",
    "duration": 120,
    "questions_count": 15,
    "category_slug": "arabic",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the Arabic term for 'contract'?",
        "explanation": "عقد (aqd) is the standard Arabic term for contract, "
                      "widely used in business and legal contexts.",
        "reference": "Business Arabic Terminology",
        "points": 1,
        "answers": [
            {"text": "اتفاق (ittifaq)", "is_correct": False},
            {"text": "عقد (aqd)", "is_correct": True},
            {"text": "وثيقة (wathiqa)", "is_correct": False},
            {"text": "صك (sakk)", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'profit' in Arabic?",
        "explanation": "ربح (ribh) is the Arabic word for profit, "
                      "fundamental in business and finance terminology.",
        "reference": "Arabic Business Vocabulary",
        "points": 1,
        "answers": [
            {"text": "خسارة (khasara)", "is_correct": False},
            {"text": "ربح (ribh)", "is_correct": True},
            {"text": "تكلفة (taklufa)", "is_correct": False},
            {"text": "دخل (dakhl)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of شركة (sharika)?",
        "explanation": "شركة (sharika) means company or corporation, "
                      "one of the most essential business terms in Arabic.",
        "reference": "Corporate Arabic Terminology",
        "points": 1,
        "answers": [
            {"text": "Partnership", "is_correct": False},
            {"text": "Company/Corporation", "is_correct": True},
            {"text": "Investment", "is_correct": False},
            {"text": "Market", "is_correct": False},
        ],
    },
    {
        "text": "Which phrase means 'customer service' in Arabic?",
        "explanation": "خدمة العملاء (khidmat al-umala) is the standard "
                      "Arabic term for customer service.",
        "reference": "Service Industry Arabic",
        "points": 2,
        "answers": [
            {"text": "خدمة العملاء (khidmat al-umala)", "is_correct": True},
            {"text": "دعم الزبائن (da'm az-zaba'in)", "is_correct": False},
            {"text": "رعاية العملاء (ri'ayat al-umala)", "is_correct": False},
            {"text": "مساعدة الزبائن (musa'adat az-zaba'in)", "is_correct": False},
        ],
    },
    {
        "text": "What does الاستثمار (al-istithmar) mean?",
        "explanation": "الاستثمار (al-istithmar) means investment, "
                      "a crucial concept in business and economics.",
        "reference": "Investment and Finance Arabic",
        "points": 1,
        "answers": [
            {"text": "Loan", "is_correct": False},
            {"text": "Investment", "is_correct": True},
            {"text": "Savings", "is_correct": False},
            {"text": "Budget", "is_correct": False},
        ],
    },
    {
        "text": "How do you express 'quality assurance' in Arabic?",
        "explanation": "ضمان الجودة (daman al-jawda) is the Arabic term "
                      "for quality assurance in business contexts.",
        "reference": "Quality Management Arabic",
        "points": 2,
        "answers": [
            {"text": "مراقبة الجودة (muraqabat al-jawda)", "is_correct": False},
            {"text": "ضمان الجودة (daman al-jawda)", "is_correct": True},
            {"text": "تحسين الجودة (tahsin al-jawda)", "is_correct": False},
            {"text": "إدارة الجودة (idarat al-jawda)", "is_correct": False},
        ],
    },
    {
        "text": "What is the Arabic term for 'marketing'?",
        "explanation": "التسويق (at-taswiq) is the standard Arabic "
                      "term for marketing in business contexts.",
        "reference": "Marketing Arabic Terminology",
        "points": 1,
        "answers": [
            {"text": "الإعلان (al-i'lan)", "is_correct": False},
            {"text": "التسويق (at-taswiq)", "is_correct": True},
            {"text": "الترويج (at-tarwij)", "is_correct": False},
            {"text": "البيع (al-bay')", "is_correct": False},
        ],
    },
    {
        "text": "Which phrase means 'human resources' in Arabic?",
        "explanation": "الموارد البشرية (al-mawarid al-bashariyya) "
                      "is the Arabic term for human resources.",
        "reference": "HR and Management Arabic",
        "points": 2,
        "answers": [
            {"text": "إدارة الأفراد (idarat al-afrad)", "is_correct": False},
            {"text": "الموارد البشرية (al-mawarid al-bashariyya)",
             "is_correct": True},
            {"text": "شؤون الموظفين (shu'un al-muwazzafin)",
             "is_correct": False},
            {"text": "قسم الأفراد (qism al-afrad)", "is_correct": False},
        ],
    },
    {
        "text": "What does محاسبة (muhasaba) refer to in business?",
        "explanation": "محاسبة (muhasaba) means accounting, "
                      "a fundamental business discipline.",
        "reference": "Accounting and Finance Arabic",
        "points": 1,
        "answers": [
            {"text": "Auditing", "is_correct": False},
            {"text": "Accounting", "is_correct": True},
            {"text": "Bookkeeping", "is_correct": False},
            {"text": "Taxation", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'supply chain' in Arabic?",
        "explanation": "سلسلة التوريد (silsilat at-tawrid) is the "
                      "Arabic term for supply chain management.",
        "reference": "Supply Chain Management Arabic",
        "points": 2,
        "answers": [
            {"text": "سلسلة الإمداد (silsilat al-imdad)", "is_correct": False},
            {"text": "سلسلة التوريد (silsilat at-tawrid)", "is_correct": True},
            {"text": "شبكة التوزيع (shabakat at-tawzi')", "is_correct": False},
            {"text": "نظام التوريد (nizam at-tawrid)", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of المدير التنفيذي (al-mudir at-tanfidhi)?",
        "explanation": "المدير التنفيذي (al-mudir at-tanfidhi) "
                      "means Chief Executive Officer (CEO).",
        "reference": "Corporate Leadership Arabic",
        "points": 2,
        "answers": [
            {"text": "General Manager", "is_correct": False},
            {"text": "Chief Executive Officer (CEO)", "is_correct": True},
            {"text": "Operations Manager", "is_correct": False},
            {"text": "Executive Assistant", "is_correct": False},
        ],
    },
    {
        "text": "Which term refers to 'market research' in Arabic?",
        "explanation": "بحث السوق (bahth as-suq) is the Arabic "
                      "term for market research.",
        "reference": "Market Analysis Arabic",
        "points": 2,
        "answers": [
            {"text": "دراسة السوق (dirasa as-suq)", "is_correct": False},
            {"text": "بحث السوق (bahth as-suq)", "is_correct": True},
            {"text": "تحليل السوق (tahlil as-suq)", "is_correct": False},
            {"text": "مراقبة السوق (muraqabat as-suq)", "is_correct": False},
        ],
    },
    {
        "text": "What does ميزانية (mizaniyya) mean in business context?",
        "explanation": "ميزانية (mizaniyya) means budget, "
                      "essential for financial planning and management.",
        "reference": "Financial Planning Arabic",
        "points": 1,
        "answers": [
            {"text": "Balance Sheet", "is_correct": False},
            {"text": "Budget", "is_correct": True},
            {"text": "Expenses", "is_correct": False},
            {"text": "Revenue", "is_correct": False},
        ],
    },
    {
        "text": "How do you express 'project management' in Arabic?",
        "explanation": "إدارة المشاريع (idarat al-masharii) is "
                      "the Arabic term for project management.",
        "reference": "Project Management Arabic",
        "points": 2,
        "answers": [
            {"text": "تنظيم المشاريع (tanzim al-masharii)", "is_correct": False},
            {"text": "إدارة المشاريع (idarat al-masharii)", "is_correct": True},
            {"text": "تخطيط المشاريع (takhtit al-masharii)", "is_correct": False},
            {"text": "تنفيذ المشاريع (tanfidh al-masharii)", "is_correct": False},
        ],
    },
    {
        "text": "What is the Arabic term for 'e-commerce'?",
        "explanation": "التجارة الإلكترونية (at-tijara al-iliktruniyya) "
                      "is the Arabic term for e-commerce.",
        "reference": "Digital Business Arabic",
        "points": 2,
        "answers": [
            {"text": "البيع الإلكتروني (al-bay' al-iliktuni)", "is_correct": False},
            {"text": "التجارة الإلكترونية (at-tijara al-iliktruniyya)",
             "is_correct": True},
            {"text": "الأعمال الرقمية (al-a'mal ar-raqamiyya)",
             "is_correct": False},
            {"text": "التسوق الإلكتروني (at-tasawwuq al-iliktuni)",
             "is_correct": False},
        ],
    }
]