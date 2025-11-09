"""
Script to populate System Design Fundamentals syllabus with detailed content for video creation.
This script creates structured content that will guide YouTube video creation.
"""

import asyncio
import sys
import json
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent.parent
sys.path.append(str(backend_path))

from database import get_db
from models import Certification
from modules.syllabus.service import SyllabusService
from sqlalchemy import select


async def populate_system_design_syllabus():
    """Populate detailed syllabus content for System Design Fundamentals"""
    
    db_gen = get_db()
    db = await db_gen.__anext__()
    
    try:
        # Get the certification
        stmt = select(Certification).where(
            Certification.slug == "system-design-fundamentals"
        )
        result = await db.execute(stmt)
        certification = result.scalar_one_or_none()
        
        if not certification:
            print("❌ System Design Fundamentals certification not found!")
            return
        
        print(f"✅ Found certification: {certification.name}")
        
        syllabus_service = SyllabusService()
        
        # Module 1: Introduction to System Design
        module1_data = {
            "module_number": 1,
            "title": "Introduction to System Design",
            "description": "Fundamental concepts and importance of system design",
            "duration": "Week 1",
            "order_index": 0,
            "learning_objectives": [
                "Understand the importance of system design",
                "Learn the basic components of a distributed system",
                "Identify common architectural patterns"
            ]
        }
        
        module1 = await syllabus_service.create_module(
            db, certification.id, module1_data
        )
        
        # Topics for Module 1
        module1_topics = [
            {
                "title": "What is System Design?",
                "description": "Understanding the fundamentals of system design",
                "introduction": "System design is the process of defining the architecture, components, modules, interfaces, and data for a system to satisfy specified requirements.",
                "order_index": 0,
                "estimated_duration": "15 minutes",
                "content": {
                    "introduction": "System design is the process of defining the architecture, components, modules, interfaces, and data for a system to satisfy specified requirements.",
                    "key_points": [
                        "Definition and scope of system design",
                        "High-level vs low-level system design", 
                        "System design vs software architecture",
                        "Real-world examples of well-designed systems"
                    ],
                    "practical_examples": [
                        "Designing a simple web application architecture",
                        "Comparing monolithic vs distributed system designs",
                        "Analyzing existing system architectures (Netflix, Uber, etc.)"
                    ],
                    "what_to_teach": [
                        "Start with a simple web app example (frontend, backend, database)",
                        "Explain the difference between functional and non-functional requirements",
                        "Show how requirements drive design decisions",
                        "Demonstrate the evolution from simple to complex systems",
                        "Discuss the importance of trade-offs in system design"
                    ]
                }
            },
            {
                "title": "Why System Design matters",
                "description": "Understanding the importance and impact of good system design",
                "introduction": "Understanding why system design is crucial for building scalable, reliable, and maintainable software systems.",
                "order_index": 1,
                "estimated_duration": "12 minutes",
                "content": {
                    "introduction": "Understanding why system design is crucial for building scalable, reliable, and maintainable software systems.",
                    "key_points": [
                        "Impact on business success and user experience",
                        "Cost implications of poor design decisions",
                        "Career advancement opportunities",
                        "Technical interview requirements"
                    ],
                    "practical_examples": [
                        "Case studies of system failures due to poor design",
                        "Success stories of well-designed systems",
                        "Cost analysis of scaling decisions"
                    ],
                    "what_to_teach": [
                        "Share real-world examples of system failures (Instagram outages, Twitter scaling issues)",
                        "Explain how good system design prevents technical debt",
                        "Discuss the relationship between system design and business metrics",
                        "Show salary differences for engineers with system design skills",
                        "Explain how system design skills help in technical leadership roles"
                    ]
                }
            },
            {
                "title": "System Design Interview Process",
                "description": "Guide to approaching system design interviews",
                "introduction": "A comprehensive guide to approaching system design interviews at top tech companies.",
                "order_index": 2,
                "estimated_duration": "20 minutes",
                "content": {
                    "introduction": "A comprehensive guide to approaching system design interviews at top tech companies.",
                    "key_points": [
                        "Structure of system design interviews",
                        "Common evaluation criteria",
                        "Time management strategies",
                        "Communication best practices"
                    ],
                    "practical_examples": [
                        "Mock interview walkthrough",
                        "Sample questions from FAANG companies",
                        "Do's and don'ts in system design interviews"
                    ],
                    "what_to_teach": [
                        "Break down the typical 45-60 minute interview structure",
                        "Teach the framework: Clarify requirements → Estimate scale → High-level design → Detailed design → Scale",
                        "Show how to ask the right clarifying questions",
                        "Demonstrate effective whiteboarding techniques",
                        "Practice common interview scenarios with time constraints"
                    ]
                }
            },
            {
                "title": "Common Architecture Patterns",
                "description": "Fundamental architectural patterns for modern systems",
                "introduction": "Fundamental architectural patterns that form the building blocks of modern distributed systems.",
                "order_index": 3,
                "estimated_duration": "18 minutes",
                "content": {
                    "introduction": "Fundamental architectural patterns that form the building blocks of modern distributed systems.",
                    "key_points": [
                        "Client-server architecture",
                        "Three-tier architecture",
                        "Microservices vs Monolithic",
                        "Event-driven architecture",
                        "Layered architecture patterns"
                    ],
                    "practical_examples": [
                        "Web application using three-tier architecture",
                        "E-commerce platform with microservices",
                        "Real-time chat application with event-driven design"
                    ],
                    "what_to_teach": [
                        "Start with simple client-server model and build complexity",
                        "Show when to use each pattern with concrete examples",
                        "Explain the pros and cons of each architectural approach",
                        "Demonstrate pattern selection based on requirements",
                        "Use visual diagrams to show data flow and component interactions"
                    ]
                }
            },
            {
                "title": "Scalability Fundamentals",
                "description": "Core principles of building scalable systems",
                "introduction": "Core principles of building systems that can handle growth in users, data, and traffic.",
                "order_index": 4,
                "estimated_duration": "16 minutes",
                "content": {
                    "introduction": "Core principles of building systems that can handle growth in users, data, and traffic.",
                    "key_points": [
                        "Definition of scalability and its types",
                        "Performance vs scalability",
                        "Identifying bottlenecks",
                        "Scalability planning and metrics"
                    ],
                    "practical_examples": [
                        "Scaling a blog from 100 to 1M users",
                        "Database scaling strategies",
                        "CDN implementation for global reach"
                    ],
                    "what_to_teach": [
                        "Define scalability with concrete numbers (RPS, concurrent users, data volume)",
                        "Explain the difference between vertical and horizontal scaling with cost analysis",
                        "Show how to identify system bottlenecks using monitoring tools",
                        "Demonstrate scalability testing and capacity planning",
                        "Discuss the relationship between scalability and system complexity"
                    ]
                }
            }
        ]
        
        # Create topics for Module 1
        for topic_data in module1_topics:
            await syllabus_service.create_topic(db, module1.id, topic_data)
        
        print(f"✅ Created Module 1 with {len(module1_topics)} topics")
        
        # Module 2: Scalability Concepts
        module2_data = {
            "module_number": 2,
            "title": "Scalability Concepts",
            "description": "Deep dive into scalability strategies and implementation",
            "duration": "Week 1-2", 
            "order_index": 1,
            "learning_objectives": [
                "Differentiate between scaling approaches",
                "Design load balancing solutions", 
                "Plan for system capacity and growth"
            ]
        }
        
        module2 = await syllabus_service.create_module(
            db, certification.id, module2_data
        )
        
        # Topics for Module 2
        module2_topics = [
            {
                "title": "Horizontal vs Vertical Scaling",
                "description": "Understanding scaling approaches and when to use each",
                "introduction": "Understanding the two fundamental approaches to scaling systems and when to use each approach.",
                "order_index": 0,
                "estimated_duration": "14 minutes",
                "content": {
                    "introduction": "Understanding the two fundamental approaches to scaling systems and when to use each approach.",
                    "key_points": [
                        "Vertical scaling: Adding more power (CPU, RAM, Storage)",
                        "Horizontal scaling: Adding more machines",
                        "Cost implications and limits of each approach",
                        "When to choose vertical vs horizontal scaling"
                    ],
                    "practical_examples": [
                        "Scaling a database server vertically (upgrading from 4GB to 32GB RAM)",
                        "Horizontal scaling with web server clusters",
                        "Real-world examples: Netflix (horizontal) vs traditional banking systems (vertical)"
                    ],
                    "what_to_teach": [
                        "Start with a simple web application serving 1000 users",
                        "Show vertical scaling: upgrading server specs and its limitations",
                        "Demonstrate horizontal scaling: adding multiple servers behind load balancer",
                        "Compare costs: $1000/month for powerful server vs $200/month × 5 smaller servers",
                        "Explain scaling limits: vertical has hardware limits, horizontal has complexity limits",
                        "Show real AWS/Azure pricing for different instance types"
                    ]
                }
            },
            {
                "title": "Load Balancing Strategies",
                "description": "Distributing traffic across multiple servers effectively",
                "introduction": "Distributing incoming requests across multiple servers to ensure optimal resource utilization and avoid overloading.",
                "order_index": 1,
                "estimated_duration": "16 minutes",
                "content": {
                    "introduction": "Distributing incoming requests across multiple servers to ensure optimal resource utilization and avoid overloading.",
                    "key_points": [
                        "Round-robin load balancing",
                        "Weighted round-robin",
                        "Least connections method",
                        "IP hash-based routing",
                        "Health checks and failover mechanisms"
                    ],
                    "practical_examples": [
                        "Setting up NGINX as a load balancer",
                        "AWS Application Load Balancer configuration",
                        "Handling server failures with health checks"
                    ],
                    "what_to_teach": [
                        "Start with the problem: 1 server getting overwhelmed, 2 servers idle",
                        "Demonstrate round-robin with simple examples (Server A, B, C rotation)",
                        "Show weighted balancing: Server A (50%), Server B (30%), Server C (20%)",
                        "Explain sticky sessions and when they're needed (shopping carts, user sessions)",
                        "Demo health checks: removing failed servers from rotation",
                        "Show real load balancer configurations and monitoring dashboards"
                    ]
                }
            }
        ]
        
        # Create topics for Module 2
        for topic_data in module2_topics:
            await syllabus_service.create_topic(db, module2.id, topic_data)
            
        print(f"✅ Created Module 2 with {len(module2_topics)} topics")
        
        await db.commit()
        print("🎉 Successfully populated System Design Fundamentals syllabus!")
        
        # Show summary
        syllabus_data = await syllabus_service.get_certification_syllabus_structured(
            db, "system-design-fundamentals"
        )
        
        if syllabus_data:
            print(f"\n📚 Syllabus Summary:")
            print(f"- Certification: {syllabus_data['certification_name']}")
            print(f"- Total Modules: {len(syllabus_data['modules'])}")
            
            total_topics = sum(len(module['topics']) for module in syllabus_data['modules'])
            print(f"- Total Topics: {total_topics}")
            
            for module in syllabus_data['modules']:
                print(f"  • Module {module['moduleNumber']}: {module['title']} ({len(module['topics'])} topics)")
    
    except Exception as e:
        print(f"❌ Error populating syllabus: {e}")
        await db.rollback()
    
    finally:
        await db.close()


if __name__ == "__main__":
    asyncio.run(populate_system_design_syllabus())