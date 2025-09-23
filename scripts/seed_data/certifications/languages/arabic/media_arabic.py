"""Media Arabic Certification"""

CERTIFICATION = {
    "name": "Media Arabic Professional",
    "description": "Arabic proficiency for journalism and media",
    "slug": "media-arabic-professional",
    "level": "Advanced",
    "duration": 135,
    "questions_count": 15,
    "category_slug": "arabic",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the Arabic term for 'breaking news'?",
        "explanation": "الأخبار العاجلة (al-akhbar al-'ajila) is the "
                      "standard term for breaking news in Arabic media.",
        "reference": "Arabic News Terminology",
        "points": 2,
        "answers": [
            {"text": "الأخبار المهمة (al-akhbar al-muhimma)", "is_correct": False},
            {"text": "الأخبار العاجلة (al-akhbar al-'ajila)", "is_correct": True},
            {"text": "الأخبار الجديدة (al-akhbar al-jadida)", "is_correct": False},
            {"text": "الأخبار الرئيسية (al-akhbar ar-ra'isiyya)",
             "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'live broadcast' in Arabic?",
        "explanation": "البث المباشر (al-bath al-mubashir) means "
                      "live broadcast in Arabic media terminology.",
        "reference": "Broadcasting Terms in Arabic",
        "points": 2,
        "answers": [
            {"text": "البث الحي (al-bath al-hayy)", "is_correct": False},
            {"text": "البث المباشر (al-bath al-mubashir)", "is_correct": True},
            {"text": "البث المفتوح (al-bath al-maftuh)", "is_correct": False},
            {"text": "البث العام (al-bath al-'amm)", "is_correct": False},
        ],
    },
    {
        "text": "What does صحفي (sahafi) mean?",
        "explanation": "صحفي (sahafi) means journalist in Arabic, "
                      "derived from صحيفة (sahifa) meaning newspaper.",
        "reference": "Media Professions in Arabic",
        "points": 1,
        "answers": [
            {"text": "Editor", "is_correct": False},
            {"text": "Journalist", "is_correct": True},
            {"text": "Photographer", "is_correct": False},
            {"text": "Reporter", "is_correct": False},
        ],
    },
    {
        "text": "Which term refers to 'editorial' in Arabic newspapers?",
        "explanation": "افتتاحية (iftitahiyya) or المقال الافتتاحي "
                      "(al-maqal al-iftitahi) refers to editorial content.",
        "reference": "Arabic Print Media Terminology",
        "points": 2,
        "answers": [
            {"text": "تحرير (tahrir)", "is_correct": False},
            {"text": "افتتاحية (iftitahiyya)", "is_correct": True},
            {"text": "رأي (ra'y)", "is_correct": False},
            {"text": "تعليق (ta'liq)", "is_correct": False},
        ],
    },
    {
        "text": "What is مراسل (murasal) in media context?",
        "explanation": "مراسل (murasal) means correspondent - a "
                      "journalist who reports from specific locations.",
        "reference": "Journalism Roles in Arabic",
        "points": 1,
        "answers": [
            {"text": "Editor", "is_correct": False},
            {"text": "Correspondent", "is_correct": True},
            {"text": "Photographer", "is_correct": False},
            {"text": "Anchor", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'press conference' in Arabic?",
        "explanation": "مؤتمر صحفي (mu'tamar sahafi) is the Arabic "
                      "term for press conference.",
        "reference": "Media Events in Arabic",
        "points": 2,
        "answers": [
            {"text": "لقاء صحفي (liqa' sahafi)", "is_correct": False},
            {"text": "مؤتمر صحفي (mu'tamar sahafi)", "is_correct": True},
            {"text": "جلسة إعلامية (jalsa i'lamiyya)", "is_correct": False},
            {"text": "ندوة صحفية (nadwa sahafiyya)", "is_correct": False},
        ],
    },
    {
        "text": "What does مذيع (mudhi') refer to?",
        "explanation": "مذيع (mudhi') means broadcaster or announcer, "
                      "commonly used for TV and radio presenters.",
        "reference": "Broadcasting Personnel in Arabic",
        "points": 1,
        "answers": [
            {"text": "Producer", "is_correct": False},
            {"text": "Broadcaster/Announcer", "is_correct": True},
            {"text": "Journalist", "is_correct": False},
            {"text": "Cameraman", "is_correct": False},
        ],
    },
    {
        "text": "Which phrase means 'exclusive interview' in Arabic?",
        "explanation": "مقابلة حصرية (muqabala hasriyya) means "
                      "exclusive interview in Arabic media.",
        "reference": "Interview Types in Arabic Media",
        "points": 2,
        "answers": [
            {"text": "مقابلة خاصة (muqabala khassa)", "is_correct": False},
            {"text": "مقابلة حصرية (muqabala hasriyya)", "is_correct": True},
            {"text": "مقابلة مهمة (muqabala muhimma)", "is_correct": False},
            {"text": "مقابلة شخصية (muqabala shakhsiyya)", "is_correct": False},
        ],
    },
    {
        "text": "What is تقرير إخباري (taqrir ikhbari)?",
        "explanation": "تقرير إخباري (taqrir ikhbari) means news "
                      "report - a journalistic account of events.",
        "reference": "News Content Types in Arabic",
        "points": 2,
        "answers": [
            {"text": "News analysis", "is_correct": False},
            {"text": "News report", "is_correct": True},
            {"text": "News summary", "is_correct": False},
            {"text": "News commentary", "is_correct": False},
        ],
    },
    {
        "text": "How do you express 'on-air' in Arabic broadcasting?",
        "explanation": "على الهواء (ala al-hawa) literally means "
                      "'on the air' and is used for live broadcasting.",
        "reference": "Broadcasting Status in Arabic",
        "points": 2,
        "answers": [
            {"text": "في البث (fi al-bath)", "is_correct": False},
            {"text": "على الهواء (ala al-hawa)", "is_correct": True},
            {"text": "في العرض (fi al-'ard)", "is_correct": False},
            {"text": "على الشاشة (ala ash-shasha)", "is_correct": False},
        ],
    },
    {
        "text": "What does محرر (muharrir) mean in journalism?",
        "explanation": "محرر (muharrir) means editor - someone who "
                      "reviews and revises content for publication.",
        "reference": "Editorial Roles in Arabic Media",
        "points": 1,
        "answers": [
            {"text": "Writer", "is_correct": False},
            {"text": "Editor", "is_correct": True},
            {"text": "Publisher", "is_correct": False},
            {"text": "Proofreader", "is_correct": False},
        ],
    },
    {
        "text": "Which term refers to 'headline' in Arabic?",
        "explanation": "عنوان رئيسي ('unwan ra'isi) or العنوان "
                      "(al-'unwan) refers to headline in Arabic newspapers.",
        "reference": "Newspaper Layout in Arabic",
        "points": 2,
        "answers": [
            {"text": "عنوان رئيسي ('unwan ra'isi)", "is_correct": True},
            {"text": "مقدمة (muqaddima)", "is_correct": False},
            {"text": "فقرة أولى (faqra ula)", "is_correct": False},
            {"text": "بداية (bidaya)", "is_correct": False},
        ],
    },
    {
        "text": "What is الإعلام المرئي (al-i'lam al-mar'i)?",
        "explanation": "الإعلام المرئي (al-i'lam al-mar'i) means "
                      "visual media, typically referring to television.",
        "reference": "Media Types in Arabic",
        "points": 2,
        "answers": [
            {"text": "Print media", "is_correct": False},
            {"text": "Visual media/Television", "is_correct": True},
            {"text": "Radio media", "is_correct": False},
            {"text": "Digital media", "is_correct": False},
        ],
    },
    {
        "text": "How do you say 'news anchor' in Arabic?",
        "explanation": "مقدم الأخبار (muqaddim al-akhbar) or "
                      "مذيع الأخبار (mudhi' al-akhbar) means news anchor.",
        "reference": "TV News Personnel in Arabic",
        "points": 2,
        "answers": [
            {"text": "مراسل الأخبار (murasal al-akhbar)", "is_correct": False},
            {"text": "مقدم الأخبار (muqaddim al-akhbar)", "is_correct": True},
            {"text": "محرر الأخبار (muharrir al-akhbar)", "is_correct": False},
            {"text": "منتج الأخبار (muntij al-akhbar)", "is_correct": False},
        ],
    },
    {
        "text": "What does البث الفضائي (al-bath al-fada'i) refer to?",
        "explanation": "البث الفضائي (al-bath al-fada'i) means "
                      "satellite broadcasting or satellite TV.",
        "reference": "Broadcasting Technology in Arabic",
        "points": 2,
        "answers": [
            {"text": "Cable TV", "is_correct": False},
            {"text": "Satellite broadcasting", "is_correct": True},
            {"text": "Internet streaming", "is_correct": False},
            {"text": "Terrestrial broadcasting", "is_correct": False},
        ],
    }
]