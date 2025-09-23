"""Environmental Science Certification"""

CERTIFICATION = {
    "name": "Environmental Science",
    "description": "Ecology, climate change, and environmental sustainability",
    "slug": "environmental-science",
    "level": "General",
    "duration": 60,
    "questions_count": 25,
    "category_slug": "environmental_science",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the greenhouse effect?",
        "explanation": (
            "The greenhouse effect is the warming of Earth's surface "
            "caused by greenhouse gases trapping heat in the atmosphere."
        ),
        "reference": "Climate Change",
        "points": 1,
        "answers": [
            {"text": "Cooling of Earth's surface", "is_correct": False},
            {"text": "Warming caused by trapped heat", "is_correct": True},
            {"text": "Ozone layer depletion", "is_correct": False},
            {"text": "Ocean acidification", "is_correct": False}
        ]
    },
    {
        "text": "What is biodiversity?",
        "explanation": (
            "Biodiversity refers to the variety of life on Earth, "
            "including diversity of species, genes, and ecosystems."
        ),
        "reference": "Ecology",
        "points": 1,
        "answers": [
            {"text": "Number of animals only", "is_correct": False},
            {"text": "Variety of all life forms", "is_correct": True},
            {"text": "Plant species only", "is_correct": False},
            {"text": "Human populations", "is_correct": False}
        ]
    },
    {
        "text": "What is renewable energy?",
        "explanation": (
            "Renewable energy comes from natural sources that "
            "replenish themselves, like solar, wind, and water power."
        ),
        "reference": "Energy Resources",
        "points": 1,
        "answers": [
            {"text": "Energy that runs out", "is_correct": False},
            {"text": "Energy from natural replenishing sources", "is_correct": True},
            {"text": "Energy from fossil fuels", "is_correct": False},
            {"text": "Nuclear energy only", "is_correct": False}
        ]
    },
    {
        "text": "What is an ecosystem?",
        "explanation": (
            "An ecosystem is a community of living organisms "
            "interacting with their physical environment."
        ),
        "reference": "Ecology",
        "points": 1,
        "answers": [
            {"text": "Only plants and animals", "is_correct": False},
            {"text": "Living things and their environment", "is_correct": True},
            {"text": "Physical environment only", "is_correct": False},
            {"text": "Human settlements", "is_correct": False}
        ]
    },
    {
        "text": "What is pollution?",
        "explanation": (
            "Pollution is the introduction of harmful substances "
            "into the environment that cause adverse changes."
        ),
        "reference": "Environmental Problems",
        "points": 1,
        "answers": [
            {"text": "Natural weather changes", "is_correct": False},
            {"text": "Harmful substances in environment", "is_correct": True},
            {"text": "Animal migration", "is_correct": False},
            {"text": "Plant growth", "is_correct": False}
        ]
    }
]