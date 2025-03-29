from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings."""
    
    # OpenAI settings
    OPENAI_API_KEY: str
    MODEL_NAME: str = "gpt-3.5-turbo"
    
    # Agent settings
    AGENT_NAME: str = "WiseDroidAgent"
    DEBUG: bool = False
    
    class Config:
        env_file = ".env"