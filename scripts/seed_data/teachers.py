from datetime import datetime, timedelta

TEST_TEACHERS = [
    {
        "user": {
            "id": "test_teacher_1",
            "name": "Dr. Sarah Johnson (TEST TEACHER)",
            "email": "sarah.test@examcenter.com",
            "email_verified": datetime.now(),
            "image": "https://i.pravatar.cc/150?img=1",
        },
        "profile": {
            "bio": "TEST TEACHER - AWS expert with 8 years experience",
            "experience_years": 8,
            "hourly_rate_one_on_one": 75.0,
            "hourly_rate_group": 45.0,
            "max_group_size": 8,
            "status": "approved",
            "is_available": True,
            "languages_spoken": '["English", "Spanish"]',
            "timezone": "America/New_York",
            "approved_at": datetime.now() - timedelta(days=30),
        },
        "qualifications": [
            {
                "category_slug": "aws",
                "certification_slug": "aws-solutions-architect-associate",
                "score_percentage": 95.0,
            }
        ]
    },
    {
        "user": {
            "id": "test_teacher_2",
            "name": "Prof. Michael Chen (TEST TEACHER)",
            "email": "michael.test@examcenter.com",
            "email_verified": datetime.now(),
            "image": "https://i.pravatar.cc/150?img=2",
        },
        "profile": {
            "bio": "TEST TEACHER - Azure expert with 10+ years",
            "experience_years": 12,
            "hourly_rate_one_on_one": 85.0,
            "hourly_rate_group": 50.0,
            "max_group_size": 10,
            "status": "approved",
            "is_available": True,
            "languages_spoken": '["English", "Mandarin"]',
            "timezone": "America/Los_Angeles",
            "approved_at": datetime.now() - timedelta(days=45),
        },
        "qualifications": [
            {
                "category_slug": "azure",
                "certification_slug": "az-900-azure-fundamentals",
                "score_percentage": 98.0,
            }
        ]
    }
]
