"""
Fix Superadmin Policies

This script adds the missing manage policies to the superadmin role.
"""
import asyncio
import sys
import os

# Add the backend directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import AsyncSessionLocal
from models import Role, Policy


async def fix_superadmin_policies():
    """Add missing policies to superadmin role"""
    async with AsyncSessionLocal() as db:
        try:
            # Get superadmin role
            role_result = await db.execute(
                select(Role).where(Role.name == "superadmin")
            )
            superadmin_role = role_result.scalar_one_or_none()
            
            if not superadmin_role:
                print("❌ Superadmin role not found!")
                return
            
            print(f"Found superadmin role: {superadmin_role.name}")
            
            # Get the new management policies
            manage_policies = ["managePolicies", "managePermissions", "manageRoles"]
            
            for policy_name in manage_policies:
                policy_result = await db.execute(
                    select(Policy).where(Policy.name == policy_name)
                )
                policy = policy_result.scalar_one_or_none()
                
                if policy:
                    # Check if policy is already assigned
                    if policy not in superadmin_role.policies:
                        superadmin_role.policies.append(policy)
                        print(f"✓ Added policy {policy_name} to superadmin")
                    else:
                        print(f"  Policy {policy_name} already assigned to superadmin")
                else:
                    print(f"❌ Policy {policy_name} not found!")
            
            # Commit changes
            await db.commit()
            print("✅ Successfully updated superadmin role with management policies!")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            await db.rollback()


if __name__ == "__main__":
    asyncio.run(fix_superadmin_policies())