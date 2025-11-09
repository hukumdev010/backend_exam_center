import asyncio
import glob
import importlib
import json
import os
import sys
from datetime import datetime
from uuid import uuid4

from seed_data.teachers import TEST_TEACHERS, TEST_STUDENTS

from database import AsyncSessionLocal, engine
from models import (
    Answer, Base, Category, Certification, Question, 
    User, TeacherProfile, TeacherQualification, QuizAttempt, TeacherStatus,
    SyllabusModule, SyllabusTopic
)
from modules.auth.service import AuthService
from modules.syllabus.service import SyllabusService

# Add parent directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def auto_discover_categories_and_certifications():
    """
    Auto-discover categories and certifications from folder structure.
    Each folder with certifications.py becomes a category.
    """
    certifications_root = os.path.join(
        os.path.dirname(__file__), "seed_data", "certifications"
    )
    
    discovered_data = {
        "categories": {},
        "certifications": [],
        "questions": {}
    }
    
    def discover_recursive(path, parent_slug=None, level=0):
        """Recursively discover categories and certifications"""
        if not os.path.isdir(path):
            return
            
        folder_name = os.path.basename(path)
        if folder_name.startswith("__"):
            return
            
        # Check if this folder has a certifications.py file
        cert_file = os.path.join(path, "certifications.py")
        has_certifications = os.path.exists(cert_file)
        
        if has_certifications:
            # This is a category with certifications
            slug = folder_name.replace("_", "-")
            
            # Create category metadata
            category_data = {
                "name": folder_name.replace("_", " ").title(),
                "slug": slug,
                "description": f"{folder_name.replace('_', ' ').title()} certifications",
                "icon": get_default_icon(folder_name),
                "color": get_default_color(folder_name),
                "parent_slug": parent_slug,
                "level": level
            }
            
            discovered_data["categories"][slug] = category_data
            
            # Load certifications from this folder
            try:
                relative_path = os.path.relpath(path, certifications_root)
                module_path = f"seed_data.certifications.{relative_path.replace(os.sep, '.')}.certifications"
                cert_module = importlib.import_module(module_path)
                
                if hasattr(cert_module, "CERTIFICATIONS"):
                    # Update category slugs in certifications to match discovered category
                    for cert in cert_module.CERTIFICATIONS:
                        cert_copy = cert.copy()
                        cert_copy["category_slug"] = slug
                        
                        # Ensure all required fields have defaults
                        cert_copy.setdefault("is_active", True)
                        cert_copy.setdefault("level", "Beginner")
                        cert_copy.setdefault("duration", 60)
                        cert_copy.setdefault("questions_count", 10)
                        
                        discovered_data["certifications"].append(cert_copy)
                    
                    print(f"  📋 {folder_name}: {len(cert_module.CERTIFICATIONS)} certifications")
                    
                    # Load questions if available
                    if hasattr(cert_module, "ALL_QUESTIONS"):
                        discovered_data["questions"].update(cert_module.ALL_QUESTIONS)
                    
                    # Try to load individual certification files for questions
                    for cert in cert_module.CERTIFICATIONS:
                        cert_slug = cert["slug"]
                        # Try to find individual certification file with questions
                        cert_files = glob.glob(os.path.join(path, "*.py"))
                        for cert_file_path in cert_files:
                            if os.path.basename(cert_file_path) == "certifications.py":
                                continue
                            if os.path.basename(cert_file_path).startswith("__"):
                                continue
                                
                            try:
                                cert_module_name = os.path.splitext(os.path.basename(cert_file_path))[0]
                                cert_module_path = f"seed_data.certifications.{relative_path.replace(os.sep, '.')}.{cert_module_name}"
                                individual_cert_module = importlib.import_module(cert_module_path)
                                
                                if hasattr(individual_cert_module, "CERTIFICATION") and hasattr(individual_cert_module, "QUESTIONS"):
                                    if individual_cert_module.CERTIFICATION.get("slug") == cert_slug:
                                        discovered_data["questions"][cert_slug] = individual_cert_module.QUESTIONS
                                        break
                            except ImportError:
                                continue
                                
            except ImportError as e:
                print(f"    ❌ Failed to load {folder_name}: {e}")
        
        # Recursively check subdirectories
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path) and not item.startswith("__"):
                    current_slug = folder_name.replace("_", "-") if has_certifications else parent_slug
                    discover_recursive(item_path, current_slug, level + 1)
        except PermissionError:
            pass
    
    print("📂 Auto-discovering categories and certifications from folder structure...")
    discover_recursive(certifications_root)
    
    return discovered_data


def get_default_icon(folder_name):
    """Get default icon based on folder name"""
    icon_map = {
        "aws": "aws",
        "azure": "azure", 
        "google_cloud": "gcp",
        "programming": "code",
        "cybersecurity": "shield",
        "data_analytics": "chart",
        "project_management": "project",
        "networking": "network",
        "database": "database",
        "linux": "linux",
        "system_design": "architecture",
        "data_structures_algorithms": "algorithm",
        "devops": "devops",
        "mathematics": "calculator",
        "physics": "atom",
        "chemistry": "test-tube",
        "biology": "dna",
        "english": "book-open",
        "german": "flag-de",
        "french": "flag-fr",
        "spanish": "flag-es",
        "italian": "flag-it",
        "japanese": "flag-jp",
        "chinese": "flag-cn",
        "korean": "flag-kr",
        "russian": "flag-ru",
        "portuguese": "flag-pt",
        "arabic": "flag-sa"
    }
    return icon_map.get(folder_name, "book")


def get_default_color(folder_name):
    """Get default color based on folder name"""
    color_map = {
        "aws": "orange",
        "azure": "blue",
        "google_cloud": "green", 
        "programming": "teal",
        "cybersecurity": "red",
        "data_analytics": "indigo",
        "project_management": "yellow",
        "networking": "cyan",
        "database": "pink",
        "linux": "gray",
        "system_design": "emerald",
        "data_structures_algorithms": "violet",
        "devops": "purple",
        "mathematics": "purple",
        "physics": "blue",
        "chemistry": "orange", 
        "biology": "emerald",
        "english": "blue",
        "german": "red",
        "french": "blue",
        "spanish": "yellow",
        "italian": "green",
        "japanese": "red",
        "chinese": "red",
        "korean": "blue",
        "russian": "blue",
        "portuguese": "green",
        "arabic": "green"
    }
    return color_map.get(folder_name, "gray")


async def create_test_teachers(session, certification_map):
    """Create test teachers with their profiles and qualifications"""
    print("👨‍🏫 Creating test teachers...")
    
    auth_service = AuthService()
    teacher_count = 0
    qualification_count = 0
    
    for teacher_data in TEST_TEACHERS:
        # Create user
        password = teacher_data["user"].get("password", "password123")  # Default password
        user = User(
            id=teacher_data["user"]["id"],
            name=teacher_data["user"]["name"],
            email=teacher_data["user"]["email"],
            email_verified=teacher_data["user"]["email_verified"],
            image=teacher_data["user"]["image"],
            password_hash=auth_service.hash_password(password),
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


async def create_test_students(session):
    """Create test students"""
    print("👨‍🎓 Creating test students...")
    
    auth_service = AuthService()
    student_count = 0
    
    for student_data in TEST_STUDENTS:
        # Create user
        password = student_data.get("password", "student123")  # Default password
        user = User(
            id=student_data["id"],
            name=student_data["name"],
            email=student_data["email"],
            email_verified=student_data["email_verified"],
            image=student_data["image"],
            password_hash=auth_service.hash_password(password),
        )
        session.add(user)
        student_count += 1
    
    print(f"✅ Created {student_count} test students")


async def create_system_design_syllabus(session, certification_map):
    """Create syllabus structure for System Design Fundamentals"""
    print("📚 Creating System Design Fundamentals syllabus...")
    
    try:
        # Get the certification
        certification = certification_map.get("system-design-fundamentals")
        if not certification:
            print("⚠️  System Design Fundamentals certification not found!")
            return
        
        # Check if certification has syllabus content
        if not certification.syllabus:
            print("⚠️  No syllabus content found in certification!")
            return
        
        syllabus_service = SyllabusService()
        
        # Parse the JSON syllabus content
        try:
            syllabus_data = json.loads(certification.syllabus)
        except (json.JSONDecodeError, TypeError) as e:
            print(f"❌ Error parsing syllabus JSON: {e}")
            return
        
        # Get modules from the JSON data
        modules = syllabus_data.get("modules", [])
        if not modules:
            print("⚠️  No modules found in syllabus data!")
            return
        
        print(f"📖 Found {len(modules)} modules in syllabus JSON")
        
        # Create modules and topics from JSON data
        for module_data in modules:
            # Create module
            module_info = {
                "module_number": module_data.get("moduleNumber", 1),
                "title": module_data.get("title", "Untitled Module"),
                "description": module_data.get("duration", ""),  # Use duration as description for now
                "duration": module_data.get("duration", ""),
                "order_index": module_data.get("moduleNumber", 1) - 1,
                "learning_objectives": module_data.get("learningObjectives", [])
            }
            
            module = await syllabus_service.create_module(
                session, certification.id, module_info
            )
            
            # Create topics for this module
            topics = module_data.get("topics", [])
            topic_count = 0
            
            for i, topic in enumerate(topics):
                # Handle both string and object topics
                if isinstance(topic, str):
                    topic_data = {
                        "title": topic,
                        "description": f"Topic {i + 1} from Module {module_data.get('moduleNumber', 1)}",
                        "introduction": "",
                        "order_index": i,
                        "estimated_duration": "15 minutes"
                    }
                elif isinstance(topic, dict):
                    topic_data = {
                        "title": topic.get("title", f"Topic {i + 1}"),
                        "description": topic.get("title", f"Topic {i + 1}"),
                        "introduction": "",
                        "order_index": i,
                        "estimated_duration": "15 minutes"
                    }
                    
                    # If topic has detailed content, extract introduction
                    if "content" in topic and isinstance(topic["content"], dict):
                        topic_data["introduction"] = topic["content"].get("introduction", "")
                else:
                    continue  # Skip invalid topic format
                
                await syllabus_service.create_topic(session, module.id, topic_data)
                topic_count += 1
            
            print(f"✅ Created Module {module_data.get('moduleNumber', '?')}: {module_info['title']} with {topic_count} topics")
        
    except Exception as e:
        print(f"❌ Error creating syllabus: {e}")
        import traceback
        traceback.print_exc()


async def populate_detailed_content(session):
    """Populate detailed content for syllabus topics"""
    print("📚 Populating detailed content for topics...")
    
    try:
        # Import the detailed content from our files
        topics_path = os.path.join(
            os.path.dirname(__file__), "seed_data", "certifications",
            "information_technology", "system_design", "syllabus",
            "fundamentals", "topics"
        )
        
        if os.path.exists(topics_path):
            sys.path.insert(0, topics_path)
            
            try:
                import what_is_system_design
                import why_system_design_matters
                import common_architecture_patterns
                import scalability_fundamentals
                
                content_map = {
                    "What is System Design?": what_is_system_design.TOPIC_CONTENT,
                    "Why System Design Matters": why_system_design_matters.TOPIC_CONTENT,
                    "Common Architecture Patterns": common_architecture_patterns.TOPIC_CONTENT,
                    "Scalability Fundamentals": scalability_fundamentals.TOPIC_CONTENT
                }
                
                # Get system design certification
                from sqlalchemy import select
                from sqlalchemy.orm import selectinload
                
                stmt = select(Certification).options(
                    selectinload(Certification.syllabus_modules).options(
                        selectinload(SyllabusModule.topics)
                    )
                ).where(
                    Certification.slug == "system-design-fundamentals"
                )
                result = await session.execute(stmt)
                certification = result.scalar_one_or_none()
                
                if certification:
                    updated_count = 0
                    
                    # Update topics with detailed content
                    for module in certification.syllabus_modules:
                        for topic in module.topics:
                            if topic.title in content_map:
                                detailed_content = content_map[topic.title]
                                
                                # Convert the content to JSON string
                                topic.detailed_content = json.dumps(
                                    detailed_content, indent=2
                                )
                                
                                updated_count += 1
                    
                    print(f"✅ Updated {updated_count} topics with detailed content")
                else:
                    print("⚠️  System Design Fundamentals certification not found")
                    
            except ImportError as e:
                print(f"⚠️  Could not import detailed content files: {e}")
            finally:
                # Remove from path
                if topics_path in sys.path:
                    sys.path.remove(topics_path)
        else:
            print("⚠️  Detailed content directory not found")
            
    except Exception as e:
        print(f"❌ Error populating detailed content: {e}")


async def seed_database():
    """Seed the database with auto-discovered certification data"""
    print("🌱 Starting database seeding with auto-discovery...")

    # Auto-discover all certifications and categories
    discovered_data = auto_discover_categories_and_certifications()
    
    categories_data = list(discovered_data["categories"].values())
    all_certifications = discovered_data["certifications"]
    all_questions = discovered_data["questions"]
    
    # Deduplicate certifications by slug
    seen_slugs = set()
    unique_certifications = []
    for cert in all_certifications:
        slug = cert.get("slug")
        if slug and slug not in seen_slugs:
            seen_slugs.add(slug)
            unique_certifications.append(cert)
        else:
            print(f"  ⚠️  Skipping duplicate certification slug: {slug}")
    
    all_certifications = unique_certifications

    print(f"📊 Found {len(categories_data)} categories and {len(all_certifications)} certifications")

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
            
            # Sort categories by level to ensure parents are created first
            categories_data.sort(key=lambda x: x["level"])
            
            # First pass: create all categories without parent relationships
            for category_data in categories_data:
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
            for category_data in categories_data:
                if category_data.get("parent_slug"):
                    parent_slug = category_data["parent_slug"]
                    if parent_slug in category_map:
                        child_category = category_map[category_data["slug"]]
                        parent_category = category_map[parent_slug]
                        child_category.parent_id = parent_category.id
            
            await session.flush()  # Update parent relationships
            print(f"✅ Created {len(categories_data)} categories with hierarchy")

            # Create certifications
            print("📜 Creating certifications...")
            certification_map = {}

            for cert_data in all_certifications:
                category_slug = cert_data["category_slug"]
                if category_slug in category_map:
                    category = category_map[category_slug]

                    certification = Certification(
                        name=cert_data.get("name", "Unknown Certification"),
                        description=cert_data.get("description", "No description available"),
                        slug=cert_data.get("slug", "unknown-cert"),
                        level=cert_data.get("level", "Beginner"),
                        duration=cert_data.get("duration", 60),
                        questions_count=cert_data.get("questions_count", 10),
                        category_id=category.id,
                        is_active=cert_data.get("is_active", True),
                        benefits=cert_data.get("benefits"),
                        advantages=cert_data.get("advantages"),
                        career_benefits=cert_data.get("career_benefits"),
                        teaching_eligibility=cert_data.get("teaching_eligibility", False),
                        min_score_for_teaching=cert_data.get("min_score_for_teaching", 90),
                        min_score_for_certificate=cert_data.get("min_score_for_certificate", 80),
                        syllabus=cert_data.get("syllabus"),
                    )
                    session.add(certification)
                    certification_map[cert_data["slug"]] = certification
                else:
                    cert_name = cert_data.get("name", "Unknown")
                    print(f"  ⚠️  Skipping certification {cert_name} - category '{category_slug}' not found")

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
                        # Ensure question has required fields
                        if not question_data.get("text"):
                            print(f"    ⚠️  Skipping question without text for {cert_slug}")
                            continue
                            
                        question = Question(
                            text=question_data.get("text", ""),
                            explanation=question_data.get("explanation", ""),
                            reference=question_data.get("reference", ""),
                            points=question_data.get("points", 1),
                            certification_id=certification.id,
                        )
                        session.add(question)
                        await session.flush()  # To get question ID
                        total_questions += 1

                        # Process answers if they exist
                        answers = question_data.get("answers", [])
                        for answer_data in answers:
                            if not answer_data.get("text"):
                                continue
                                
                            answer = Answer(
                                text=answer_data.get("text", ""),
                                is_correct=answer_data.get("is_correct", False),
                                question_id=question.id,
                            )
                            session.add(answer)
                            total_answers += 1

            print(f"✅ Created {total_questions} questions with {total_answers} answer options")

            # Create test teachers with their profiles and qualifications
            await create_test_teachers(session, certification_map)

            # Create test students
            await create_test_students(session)

            # Create syllabus structure for System Design Fundamentals
            await create_system_design_syllabus(session, certification_map)

            # Populate detailed content for syllabus topics
            await populate_detailed_content(session)

            # Commit all changes
            await session.commit()

            # Print summary
            print("\n🎉 Database seeding completed successfully!")
            print("=" * 60)
            print("SEEDING SUMMARY:")
            print(f"📁 Categories: {len(categories_data)}")
            print(f"📜 Certifications: {len(certification_map)}")
            print(f"❓ Questions: {total_questions}")
            print(f"✅ Answer Options: {total_answers}")
            print(f"👨‍🏫 Test Teachers: {len(TEST_TEACHERS)}")
            print(f"👨‍🎓 Test Students: {len(TEST_STUDENTS)}")
            print("=" * 60)

            # Print breakdown by category
            print("\nCERTIFICATIONS BY CATEGORY:")
            for category_data in categories_data:
                cert_count = sum(
                    1
                    for cert in all_certifications
                    if cert["category_slug"] == category_data["slug"]
                )
                print(f"  {category_data['name']}: {cert_count} certifications")

        except Exception as e:
            print(f"❌ Error seeding database: {e}")
            await session.rollback()
            raise


if __name__ == "__main__":
    asyncio.run(seed_database())