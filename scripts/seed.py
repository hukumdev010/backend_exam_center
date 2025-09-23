import asyncio
import glob
import importlib
import os
import sys
from datetime import datetime
from uuid import uuid4

from seed_data.categories import CATEGORIES
from seed_data.teachers import TEST_TEACHERS

from database import AsyncSessionLocal, engine
from models import (
    Answer, Base, Category, Certification, Question, 
    User, TeacherProfile, TeacherQualification, QuizAttempt, TeacherStatus
)

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Import seed data


async def create_test_teachers(session, certification_map):
    """Create test teachers with their profiles and qualifications"""
    print("👨‍🏫 Creating test teachers...")
    
    teacher_count = 0
    qualification_count = 0
    
    for teacher_data in TEST_TEACHERS:
        # Create user
        user = User(
            id=teacher_data["user"]["id"],
            name=teacher_data["user"]["name"],
            email=teacher_data["user"]["email"],
            email_verified=teacher_data["user"]["email_verified"],
            image=teacher_data["user"]["image"],
        )
        session.add(user)
        await session.flush()  # To get user ID
        
        # Create teacher profile
        profile_data = teacher_data["profile"]
        
        # Convert string status to enum
        status_str = profile_data["status"]
        if status_str == "approved":
            status_enum = TeacherStatus.APPROVED
        elif status_str == "pending":
            status_enum = TeacherStatus.PENDING
        elif status_str == "rejected":
            status_enum = TeacherStatus.REJECTED
        elif status_str == "suspended":
            status_enum = TeacherStatus.SUSPENDED
        else:
            status_enum = TeacherStatus.PENDING  # Default fallback
            
        profile = TeacherProfile(
            user_id=user.id,
            bio=profile_data["bio"],
            experience_years=profile_data["experience_years"],
            hourly_rate_one_on_one=profile_data["hourly_rate_one_on_one"],
            hourly_rate_group=profile_data["hourly_rate_group"],
            max_group_size=profile_data["max_group_size"],
            status=status_enum,
            is_available=profile_data["is_available"],
            languages_spoken=profile_data["languages_spoken"],
            timezone=profile_data["timezone"],
            approved_at=profile_data["approved_at"],
        )
        session.add(profile)
        await session.flush()  # To get profile ID
        teacher_count += 1
        
        # Create teacher qualifications
        for qual_data in teacher_data["qualifications"]:
            cert_slug = qual_data["certification_slug"]
            if cert_slug in certification_map:
                certification = certification_map[cert_slug]
                
                # Create a mock quiz attempt
                quiz_attempt = QuizAttempt(
                    id=f"test_attempt_{user.id}_{cert_slug}",
                    user_id=user.id,
                    certification_id=certification.id,
                    score=int(qual_data["score_percentage"]),
                    total_questions=100,
                    correct_answers=int(qual_data["score_percentage"]),
                    points=int(qual_data["score_percentage"]),
                    completed_at=datetime.now(),
                )
                session.add(quiz_attempt)
                await session.flush()
                
                # Create teacher qualification
                qualification = TeacherQualification(
                    user_id=user.id,
                    category_id=certification.category_id,
                    certification_id=certification.id,
                    quiz_attempt_id=quiz_attempt.id,
                    score_percentage=qual_data["score_percentage"],
                )
                session.add(qualification)
                qualification_count += 1
    
    print(f"✅ Created {teacher_count} test teachers with "
          f"{qualification_count} qualifications")


def load_all_certifications():
    """Dynamically load all certifications from the organized folder structure"""
    certifications_root = os.path.join(
        os.path.dirname(__file__), "seed_data", "certifications"
    )
    all_certifications = []
    all_questions = {}

    # Get all category folders
    category_folders = [
        f
        for f in os.listdir(certifications_root)
        if os.path.isdir(os.path.join(certifications_root, f))
        and not f.startswith("__")
    ]

    for category_folder in category_folders:
        # Handle nested structure (languages, academic)
        if category_folder in ["languages", "academic"]:
            print(f"  📁 Processing {category_folder} subfolder...")
            category_path = os.path.join(certifications_root, category_folder)
            subcategory_folders = [
                f for f in os.listdir(category_path)
                if os.path.isdir(os.path.join(category_path, f))
                and not f.startswith("__")
            ]
            
            for subcategory_folder in subcategory_folders:
                try:
                    # Try to load certifications from subcategory
                    cert_file = os.path.join(
                        category_path, subcategory_folder, "certifications.py"
                    )
                    if os.path.exists(cert_file):
                        module_path = (f"seed_data.certifications.{category_folder}."
                                     f"{subcategory_folder}.certifications")
                        cert_module = importlib.import_module(module_path)
                        
                        if hasattr(cert_module, "CERTIFICATIONS"):
                            all_certifications.extend(cert_module.CERTIFICATIONS)
                            print(
                                f"    📋 {subcategory_folder}: "
                                f"{len(cert_module.CERTIFICATIONS)} certifications loaded"
                            )
                            
                except ImportError as e:
                    print(f"    ❌ Failed to load {subcategory_folder}: {e}")
            continue
            
        # Handle existing IT category structure
        try:
            # Try to import the category module (organized structure)
            module_path = f"seed_data.certifications.{category_folder}"
            category_module = importlib.import_module(module_path)

            if hasattr(category_module, "CERTIFICATIONS"):
                all_certifications.extend(category_module.CERTIFICATIONS)
                print(
                    f"  📋 {category_folder}: {len(category_module.CERTIFICATIONS)} certifications loaded"
                )

                if hasattr(category_module, "ALL_QUESTIONS"):
                    all_questions.update(category_module.ALL_QUESTIONS)

        except ImportError as e:
            print(
                f"  ⚠️  {category_folder}: No organized module found, trying individual files"
            )

            # Fallback: try to load individual certification files
            category_path = os.path.join(certifications_root, category_folder)
            cert_files = glob.glob(os.path.join(category_path, "*.py"))

            category_certs = []
            category_questions = {}

            for cert_file in cert_files:
                if os.path.basename(cert_file).startswith("__"):
                    continue

                try:
                    cert_module_name = os.path.splitext(
                        os.path.basename(cert_file))[0]
                    cert_module_path = (
                        f"seed_data.certifications.{category_folder}.{cert_module_name}"
                    )
                    cert_module = importlib.import_module(cert_module_path)

                    if hasattr(cert_module, "CERTIFICATION"):
                        category_certs.append(cert_module.CERTIFICATION)

                        if hasattr(cert_module,
                                   "QUESTIONS") and cert_module.QUESTIONS:
                            category_questions[cert_module.CERTIFICATION["slug"]] = (
                                cert_module.QUESTIONS)

                except ImportError as cert_e:
                    print(f"    ❌ Failed to load {cert_module_name}: {cert_e}")

            if category_certs:
                all_certifications.extend(category_certs)
                all_questions.update(category_questions)
                print(
                    f"  📋 {category_folder}: {len(category_certs)} certifications loaded (individual files)"
                )

    # Load legacy flat files only for categories that don't have organized
    # structure
    try:
        # Only load legacy modules that don't have organized counterparts
        legacy_modules = []
        for module_name in [
            "azure",
            "google_cloud",
            "devops",
            "programming",
            "data_analytics",
            "project_management",
            "networking",
            "database",
        ]:
            if module_name not in category_folders:
                try:
                    module = importlib.import_module(
                        f"seed_data.certifications.{module_name}"
                    )
                    legacy_modules.append((module_name, module))
                except ImportError:
                    continue

        for module_name, module in legacy_modules:
            if hasattr(module, "CERTIFICATIONS"):
                all_certifications.extend(module.CERTIFICATIONS)
                print(
                    f"  📋 {module_name} (legacy): {len(module.CERTIFICATIONS)} certifications"
                )

                if hasattr(module, "QUESTIONS"):
                    all_questions.update(module.QUESTIONS)

    except ImportError as e:
        print(f"  ℹ️  No legacy certification modules found: {e}")

    return all_certifications, all_questions


async def seed_database():
    """Seed the database with comprehensive certification data"""
    print("🌱 Starting comprehensive database seeding with organized structure...")

    # Load all certifications dynamically
    print("📂 Loading certifications from organized folder structure...")
    all_certifications, all_questions = load_all_certifications()

    print(
        f"📊 Found {len(CATEGORIES)} categories and {len(all_certifications)} certifications"
    )

    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tables created")

    async with AsyncSessionLocal() as session:
        try:
            # Create categories with hierarchy support
            print("📁 Creating categories...")
            category_map = {}
            
            # First pass: create all categories without parent relationships
            for category_data in CATEGORIES:
                category = Category(
                    name=category_data["name"],
                    description=category_data["description"],
                    slug=category_data["slug"],
                    icon=category_data["icon"],
                    color=category_data["color"],
                )
                session.add(category)
                category_map[category_data["slug"]] = category

            await session.flush()  # To get category IDs
            
            # Second pass: set parent relationships
            for category_data in CATEGORIES:
                if "parent_slug" in category_data:
                    parent_slug = category_data["parent_slug"]
                    if parent_slug in category_map:
                        child_category = category_map[category_data["slug"]]
                        parent_category = category_map[parent_slug]
                        child_category.parent_id = parent_category.id
            
            await session.flush()  # Update parent relationships
            print(f"✅ Created {len(CATEGORIES)} categories with hierarchy")

            # Create certifications
            print("📜 Creating certifications...")
            certification_map = {}

            for cert_data in all_certifications:
                category_slug = cert_data["category_slug"]
                if category_slug in category_map:
                    category = category_map[category_slug]

                    certification = Certification(
                        name=cert_data["name"],
                        description=cert_data["description"],
                        slug=cert_data["slug"],
                        level=cert_data["level"],
                        duration=cert_data["duration"],
                        questions_count=cert_data["questions_count"],
                        category_id=category.id,
                        is_active=cert_data["is_active"],
                    )
                    session.add(certification)
                    certification_map[cert_data["slug"]] = certification
                else:
                    print(
                        f"  ⚠️  Skipping certification {cert_data['name']} - category '{category_slug}' not found"
                    )

            await session.flush()  # To get certification IDs
            print(f"✅ Created {len(certification_map)} certifications")

            # Create questions and answers
            print("❓ Creating questions and answers...")
            total_questions = 0
            total_answers = 0

            for cert_slug, questions_data in all_questions.items():
                if cert_slug in certification_map:
                    certification = certification_map[cert_slug]

                    for question_data in questions_data:
                        question = Question(
                            text=question_data["text"],
                            explanation=question_data["explanation"],
                            reference=question_data.get("reference", ""),
                            points=question_data.get("points", 1),
                            certification_id=certification.id,
                        )
                        session.add(question)
                        await session.flush()  # To get question ID
                        total_questions += 1

                        for answer_data in question_data["answers"]:
                            answer = Answer(
                                text=answer_data["text"],
                                is_correct=answer_data["is_correct"],
                                question_id=question.id,
                            )
                            session.add(answer)
                            total_answers += 1

            print(
                f"✅ Created {total_questions} questions with {total_answers} answer options"
            )

            # Create test teachers with their profiles and qualifications
            await create_test_teachers(session, certification_map)

            # Commit all changes
            await session.commit()

            # Print summary
            print("\n🎉 Database seeding completed successfully!")
            print("=" * 60)
            print("SEEDING SUMMARY:")
            print(f"📁 Categories: {len(CATEGORIES)}")
            print(f"📜 Certifications: {len(certification_map)}")
            print(f"❓ Questions: {total_questions}")
            print(f"✅ Answer Options: {total_answers}")
            print(f"👨‍🏫 Test Teachers: {len(TEST_TEACHERS)}")
            print("=" * 60)

            # Print breakdown by category
            print("\nCERTIFICATIONS BY CATEGORY:")
            for category_data in CATEGORIES:
                cert_count = sum(
                    1
                    for cert in all_certifications
                    if cert["category_slug"] == category_data["slug"]
                )
                print(
                    f"  {category_data['name']}: {cert_count} certifications")

        except Exception as e:
            print(f"❌ Error seeding database: {e}")
            await session.rollback()
            raise


if __name__ == "__main__":
    asyncio.run(seed_database())
