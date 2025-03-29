import pytest
from app.agent.base import BaseAgent
from app.config.settings import Settings

@pytest.fixture
def agent():
    return BaseAgent()

def test_agent_initialization(agent):
    assert isinstance(agent.settings, Settings)
    assert isinstance(agent.agent_config, dict)

@pytest.mark.asyncio
async def test_agent_process():
    agent = BaseAgent()
    # This test will be expanded when actual agent processing is implemented
    await agent.process("test input")
    assert True  # Placeholder assertion