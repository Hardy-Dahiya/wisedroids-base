from typing import List
from langchain.tools import BaseTool

class BaseAgentTool(BaseTool):
    """Base class for all WiseDroidAI agent tools."""
    
    def __init__(self):
        super().__init__()
    
    def _run(self, *args, **kwargs):
        """
        Execute the tool.
        This method will be implemented by specific tools.
        """
        raise NotImplementedError()

    async def _arun(self, *args, **kwargs):
        """
        Execute the tool asynchronously.
        This method will be implemented by specific tools.
        """
        raise NotImplementedError()