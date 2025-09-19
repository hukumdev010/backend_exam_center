"""
Test script for the new teacher-student system APIs
"""
import asyncio
import sys
import os

# Add backend to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import get_db
from models import *
from modules.teachers.service import TeacherService
from modules.sessions.service import SessionService


async def test_teacher_system():
    """Test the teacher-student system functionality"""
    
    print("🧪 Testing Teacher-Student System")
    print("=" * 50)
    
    async for db in get_db():
        try:
            # Test 1: Check teaching eligibility
            test_user_id = "test_user_123"
            print(f"1. Checking eligibility for user: {test_user_id}")
            
            eligibility = await TeacherService.check_teaching_eligibility(
                db, test_user_id
            )
            print(f"   Eligibility: {eligibility}")
            
            # Test 2: List available sessions
            print("\n2. Listing available sessions...")
            sessions = await SessionService.get_available_sessions(db, limit=5)
            print(f"   Found {len(sessions)} available sessions")
            
            print("\n✅ Basic functionality tests completed!")
            
        except Exception as e:
            print(f"❌ Test failed: {e}")
            import traceback
            traceback.print_exc()
        
        break  # Exit after first iteration


if __name__ == "__main__":
    asyncio.run(test_teacher_system())