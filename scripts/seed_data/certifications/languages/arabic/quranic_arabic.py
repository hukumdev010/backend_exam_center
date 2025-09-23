"""Quranic Arabic Certification"""

CERTIFICATION = {
    "name": "Quranic Arabic Proficiency",
    "description": "Classical Arabic proficiency for Quranic studies and texts",
    "slug": "quranic-arabic-proficiency",
    "level": "Intermediate to Advanced",
    "duration": 150,
    "questions_count": 20,
    "category_slug": "arabic",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What does بسم الله الرحمن الرحيم (Bismillahi Rahmani Raheem) mean?",
        "explanation": "This is the Basmala, meaning 'In the name of Allah, "
                      "the Most Gracious, the Most Merciful'.",
        "reference": "Quranic Opening Formula",
        "points": 1,
        "answers": [
            {"text": "Praise be to Allah", "is_correct": False},
            {"text": "In the name of Allah, the Most Gracious, "
                     "the Most Merciful", "is_correct": True},
            {"text": "There is no god but Allah", "is_correct": False},
            {"text": "Allah is the Greatest", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of الحمد لله رب العالمين (Alhamdulillahi "
               "Rabbil Alameen)?",
        "explanation": "This phrase means 'All praise is due to Allah, "
                      "Lord of all the worlds' - the opening of Surah Al-Fatiha.",
        "reference": "Surah Al-Fatiha, Verse 2",
        "points": 2,
        "answers": [
            {"text": "In the name of Allah", "is_correct": False},
            {"text": "All praise is due to Allah, Lord of all the worlds",
             "is_correct": True},
            {"text": "Guide us to the straight path", "is_correct": False},
            {"text": "You alone we worship", "is_correct": False},
        ],
    },
    {
        "text": "What does إياك نعبد وإياك نستعين (Iyyaka na'budu wa iyyaka "
               "nasta'een) mean?",
        "explanation": "This means 'You alone we worship, and You alone "
                      "we ask for help' from Surah Al-Fatiha.",
        "reference": "Surah Al-Fatiha, Verse 5",
        "points": 2,
        "answers": [
            {"text": "You alone we worship, and You alone we ask for help",
             "is_correct": True},
            {"text": "Guide us to the straight path", "is_correct": False},
            {"text": "Show us the straight way", "is_correct": False},
            {"text": "Master of the Day of Judgment", "is_correct": False},
        ],
    },
    {
        "text": "What is الصراط المستقيم (As-Sirat Al-Mustaqeem)?",
        "explanation": "الصراط المستقيم means 'the straight path' - "
                      "referring to the path of righteousness and guidance.",
        "reference": "Surah Al-Fatiha, Verse 6",
        "points": 2,
        "answers": [
            {"text": "The Day of Judgment", "is_correct": False},
            {"text": "The straight path", "is_correct": True},
            {"text": "The Book of Allah", "is_correct": False},
            {"text": "The worship of Allah", "is_correct": False},
        ],
    },
    {
        "text": "What does تبارك الله (Tabarakallah) express?",
        "explanation": "تبارك الله means 'Blessed is Allah' - "
                      "an expression of praise and recognition of Allah's blessings.",
        "reference": "Quranic Praise Expressions",
        "points": 1,
        "answers": [
            {"text": "God willing", "is_correct": False},
            {"text": "Blessed is Allah", "is_correct": True},
            {"text": "Glory be to Allah", "is_correct": False},
            {"text": "Allah is Great", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of سبحان الله (Subhanallah)?",
        "explanation": "سبحان الله means 'Glory be to Allah' or "
                      "'Allah is perfect' - expressing Allah's transcendence.",
        "reference": "Tasbih in the Quran",
        "points": 1,
        "answers": [
            {"text": "Praise be to Allah", "is_correct": False},
            {"text": "Glory be to Allah", "is_correct": True},
            {"text": "Allah is the Greatest", "is_correct": False},
            {"text": "In the name of Allah", "is_correct": False},
        ],
    },
    {
        "text": "What does الله أكبر (Allahu Akbar) mean?",
        "explanation": "الله أكبر means 'Allah is Greatest' - "
                      "the Takbir used in prayer and expressions of praise.",
        "reference": "Takbir in Islamic Practice",
        "points": 1,
        "answers": [
            {"text": "Allah is One", "is_correct": False},
            {"text": "Allah is Greatest", "is_correct": True},
            {"text": "Allah is Merciful", "is_correct": False},
            {"text": "Allah knows best", "is_correct": False},
        ],
    },
    {
        "text": "What is يوم الدين (Yawm Ad-Deen)?",
        "explanation": "يوم الدين means 'the Day of Judgment' or "
                      "'the Day of Religion' - the Day of Final Judgment.",
        "reference": "Surah Al-Fatiha, Verse 4",
        "points": 2,
        "answers": [
            {"text": "Day of Prayer", "is_correct": False},
            {"text": "Day of Judgment", "is_correct": True},
            {"text": "Day of Creation", "is_correct": False},
            {"text": "Day of Worship", "is_correct": False},
        ],
    },
    {
        "text": "What does استغفر الله (Astaghfirullah) mean?",
        "explanation": "استغفر الله means 'I seek forgiveness from Allah' - "
                      "a phrase used to seek Allah's forgiveness.",
        "reference": "Seeking Forgiveness in Islam",
        "points": 1,
        "answers": [
            {"text": "I praise Allah", "is_correct": False},
            {"text": "I seek forgiveness from Allah", "is_correct": True},
            {"text": "I trust in Allah", "is_correct": False},
            {"text": "I thank Allah", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of إن شاء الله (In Sha Allah)?",
        "explanation": "إن شاء الله means 'If Allah wills' or "
                      "'God willing' - expressing reliance on Allah's will.",
        "reference": "Conditional Expressions in Arabic",
        "points": 1,
        "answers": [
            {"text": "With Allah's blessing", "is_correct": False},
            {"text": "If Allah wills", "is_correct": True},
            {"text": "Thanks to Allah", "is_correct": False},
            {"text": "For Allah's sake", "is_correct": False},
        ],
    },
    {
        "text": "What does لا إله إلا الله (La ilaha illa Allah) declare?",
        "explanation": "لا إله إلا الله is the Shahada, declaring "
                      "'There is no god but Allah' - the fundamental Islamic creed.",
        "reference": "The Shahada (Declaration of Faith)",
        "points": 2,
        "answers": [
            {"text": "Allah is the Greatest", "is_correct": False},
            {"text": "There is no god but Allah", "is_correct": True},
            {"text": "Muhammad is the Messenger", "is_correct": False},
            {"text": "Prayer is obligatory", "is_correct": False},
        ],
    },
    {
        "text": "What is تقوى الله (Taqwa Allah)?",
        "explanation": "تقوى الله means 'fear of Allah' or "
                      "'God-consciousness' - being mindful of Allah in all actions.",
        "reference": "Concept of Taqwa in Islam",
        "points": 2,
        "answers": [
            {"text": "Love of Allah", "is_correct": False},
            {"text": "Fear of Allah/God-consciousness", "is_correct": True},
            {"text": "Worship of Allah", "is_correct": False},
            {"text": "Trust in Allah", "is_correct": False},
        ],
    },
    {
        "text": "What does بارك الله فيك (Barakallahu feek) mean?",
        "explanation": "بارك الله فيك means 'May Allah bless you' - "
                      "a common blessing and expression of good wishes.",
        "reference": "Islamic Blessings and Du'as",
        "points": 1,
        "answers": [
            {"text": "Allah protect you", "is_correct": False},
            {"text": "May Allah bless you", "is_correct": True},
            {"text": "Allah be with you", "is_correct": False},
            {"text": "Thank you", "is_correct": False},
        ],
    },
    {
        "text": "What is المغضوب عليهم (Al-maghdubi alayhim)?",
        "explanation": "المغضوب عليهم means 'those who have "
                      "earned [Your] anger' from the final verse of Al-Fatiha.",
        "reference": "Surah Al-Fatiha, Verse 7",
        "points": 2,
        "answers": [
            {"text": "The righteous", "is_correct": False},
            {"text": "Those who have earned [Your] anger", "is_correct": True},
            {"text": "The believers", "is_correct": False},
            {"text": "The guided ones", "is_correct": False},
        ],
    },
    {
        "text": "What does الضالين (Ad-Dalleen) refer to?",
        "explanation": "الضالين means 'those who have gone astray' - "
                      "referring to those who have lost the right path.",
        "reference": "Surah Al-Fatiha, Verse 7",
        "points": 2,
        "answers": [
            {"text": "The believers", "is_correct": False},
            {"text": "Those who have gone astray", "is_correct": True},
            {"text": "The righteous", "is_correct": False},
            {"text": "The blessed", "is_correct": False},
        ],
    },
    {
        "text": "What is جزاك الله خيرا (Jazakallahu khayran)?",
        "explanation": "جزاك الله خيرا means 'May Allah reward you "
                      "with good' - an expression of gratitude and blessing.",
        "reference": "Islamic Expressions of Gratitude",
        "points": 1,
        "answers": [
            {"text": "Thank you very much", "is_correct": False},
            {"text": "May Allah reward you with good", "is_correct": True},
            {"text": "Allah bless you", "is_correct": False},
            {"text": "May Allah guide you", "is_correct": False},
        ],
    },
    {
        "text": "What does حسبنا الله ونعم الوكيل (Hasbunallahu wa ni'mal wakeel) "
               "express?",
        "explanation": "This means 'Allah is sufficient for us, "
                      "and He is the best disposer of affairs' - expressing "
                      "trust in Allah.",
        "reference": "Quranic Expressions of Trust",
        "points": 2,
        "answers": [
            {"text": "Praise be to Allah", "is_correct": False},
            {"text": "Allah is sufficient for us, and He is the best "
                     "disposer of affairs", "is_correct": True},
            {"text": "We seek refuge in Allah", "is_correct": False},
            {"text": "Allah is our Lord", "is_correct": False},
        ],
    },
    {
        "text": "What is the meaning of آمين (Ameen)?",
        "explanation": "آمين means 'Amen' - used to conclude "
                      "supplications, meaning 'So be it' or 'May it be so'.",
        "reference": "Concluding Supplications",
        "points": 1,
        "answers": [
            {"text": "God willing", "is_correct": False},
            {"text": "Amen/So be it", "is_correct": True},
            {"text": "Praise Allah", "is_correct": False},
            {"text": "Thank Allah", "is_correct": False},
        ],
    },
    {
        "text": "What does رب اغفر لي (Rabbi ghfir li) mean?",
        "explanation": "رب اغفر لي means 'My Lord, forgive me' - "
                      "a common supplication seeking Allah's forgiveness.",
        "reference": "Personal Supplications in Arabic",
        "points": 1,
        "answers": [
            {"text": "My Lord, guide me", "is_correct": False},
            {"text": "My Lord, forgive me", "is_correct": True},
            {"text": "My Lord, help me", "is_correct": False},
            {"text": "My Lord, bless me", "is_correct": False},
        ],
    },
    {
        "text": "What is المهتدين (Al-Muhtadeen)?",
        "explanation": "المهتدين means 'those who are guided' - "
                      "referring to people who follow the right path.",
        "reference": "Quranic Terms for Guidance",
        "points": 2,
        "answers": [
            {"text": "Those who are lost", "is_correct": False},
            {"text": "Those who are guided", "is_correct": True},
            {"text": "Those who are blessed", "is_correct": False},
            {"text": "Those who worship", "is_correct": False},
        ],
    }
]