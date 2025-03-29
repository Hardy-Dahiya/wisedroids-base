from langchain.agents import AgentExecutor
from langchain.chains import LLMChain
from app.config.settings import Settings

class BaseAgent:
    def __init__(self):
        self.settings = Settings()
        # Agent configuration will be inserted here by WiseDroidAI
        self.agent_config = {}
    
    async def initialize(self):
        """
        Initialize the agent with the configuration.
        This method will be populated by WiseDroidAI generated code.
        """
        pass

    async def process(self, user_input: str):
        """
        Process user input and return response.
        This method will be populated by WiseDroidAI generated code.
        """
        pass