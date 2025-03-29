from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from app.agent.base import BaseAgent

router = APIRouter()
agent = BaseAgent()

class AgentInput(BaseModel):
    message: str
    context: Dict[str, Any] = {}

class AgentResponse(BaseModel):
    response: str
    metadata: Dict[str, Any] = {}

@router.post("/chat", response_model=AgentResponse)
async def chat_with_agent(input_data: AgentInput):
    try:
        response = await agent.process(input_data.message)
        return AgentResponse(
            response=response,
            metadata={"status": "success"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))