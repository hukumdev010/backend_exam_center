import google.generativeai as genai
from fastapi import HTTPException

from settings.loader import get_settings


class AIAssistantService:
    def __init__(self):
        pass

    async def chat_with_ai(self, message: str, context: str = None, current_question: str = None, conversation_history: list = None):
        """Chat with AI assistant for exam help"""
        try:
            # Get settings with API key
            settings = await get_settings()
            gemini_api_key = settings.gemini_api_key

            if not gemini_api_key:
                return {
                    "response": (
                        "I'm sorry, but the AI assistant is currently "
                        "unavailable. Please try again later."
                    ),
                    "error": "Gemini API key not configured",
                }

            # Configure Gemini API with key from settings
            genai.configure(api_key=gemini_api_key)

            # Create the model
            model = genai.GenerativeModel("gemini-pro")

            # Build conversation context
            system_prompt = """You are an AI tutor specializing in certification exams. 
            You help students understand concepts, explain answers, and provide study guidance.
            Keep responses helpful, educational, and encouraging. If you're unsure about something,
            say so rather than guessing."""

            # Add context if provided
            if context:
                system_prompt += f"\n\nContext: {context}"

            if current_question:
                system_prompt += f"\n\nCurrent Question: {current_question}"

            # Build conversation history
            conversation = f"{system_prompt}\n\nUser: {message}"

            if conversation_history:
                for msg in conversation_history[-5:]:  # Keep last 5 messages
                    role = "User" if msg.get("is_user") else "Assistant"
                    conversation = f"{role}: {msg.get('content')}\n" + conversation

            # Generate response
            response = model.generate_content(conversation)
            return {"response": response.text, "error": None}

        except Exception as e:
            return {
                "response": "I'm sorry, I encountered an error. Please try again.",
                "error": str(e)
            }

    async def ai_health(self):
        """Check AI service health"""
        try:
            settings = await get_settings()
            gemini_api_key = settings.gemini_api_key

            if not gemini_api_key:
                return {
                    "status": "unhealthy",
                    "error": "Gemini API key not configured"
                }

            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel("gemini-pro")
            
            # Test with a simple prompt
            response = model.generate_content("Hello, are you working?")
            
            return {
                "status": "healthy",
                "model": "gemini-pro",
                "test_response": response.text[:100] + "..." if len(response.text) > 100 else response.text
            }
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e)
            }

    async def list_models(self):
        """List available AI models"""
        try:
            settings = await get_settings()
            gemini_api_key = settings.gemini_api_key

            if not gemini_api_key:
                return {
                    "models": [],
                    "error": "Gemini API key not configured"
                }

            genai.configure(api_key=gemini_api_key)
            models = []
            
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    models.append({
                        "name": m.name,
                        "display_name": m.display_name,
                        "description": m.description
                    })

            return {"models": models, "error": None}
        except Exception as e:
            return {
                "models": [],
                "error": str(e)
            }

    async def generate_study_prompt(
        self, certification_name: str, category: str = None, level: str = None, user_progress: int = None
    ):
        """Generate a personalized study prompt"""
        try:
            settings = await get_settings()
            gemini_api_key = settings.gemini_api_key

            if not gemini_api_key:
                return {
                    "prompt": "AI assistant is currently unavailable.",
                    "error": "Gemini API key not configured"
                }

            genai.configure(api_key=gemini_api_key)
            model = genai.GenerativeModel("gemini-pro")

            # Build the prompt
            prompt_request = f"""
            Generate a personalized study prompt for the {certification_name} certification.
            """

            if category:
                prompt_request += f" This is in the {category} category."
            
            if level:
                prompt_request += f" The difficulty level is {level}."
            
            if user_progress:
                prompt_request += f" The user is {user_progress}% through their preparation."

            prompt_request += """
            
            Please provide:
            1. A motivational opening
            2. Key areas to focus on
            3. Study tips specific to this certification
            4. A suggested daily routine
            
            Keep it encouraging and actionable.
            """

            response = model.generate_content(prompt_request)
            return {"prompt": response.text, "error": None}

        except Exception as e:
            return {
                "prompt": "Unable to generate study prompt at this time.",
                "error": str(e)
            }