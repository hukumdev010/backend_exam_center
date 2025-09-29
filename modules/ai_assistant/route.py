from fastapi import APIRouter, Depends

from modules.rbac.decorators import require_policies
from .controller import AIAssistantController
from .model import (
    ChatRequest, ChatResponse, StudyPromptRequest, StudyPromptResponse
)

router = APIRouter()
ai_controller = AIAssistantController()


@router.post("/chat", response_model=ChatResponse,
             dependencies=[Depends(require_policies("useAIAssistant"))])
async def chat_with_ai(request: ChatRequest):
    """Chat with AI assistant for exam help"""
    return await ai_controller.chat_with_ai(request.dict())


@router.get("/health")
async def ai_health():
    """Check AI service health status"""
    return await ai_controller.ai_health()


@router.get("/models")
async def list_models():
    """List available AI models"""
    return await ai_controller.list_models()


@router.post("/study-prompt", response_model=StudyPromptResponse,
             dependencies=[Depends(require_policies("useAIAssistant"))])
async def generate_study_prompt(request: StudyPromptRequest):
    """Generate a personalized study prompt for a certification"""
    return await ai_controller.generate_study_prompt(request.dict())