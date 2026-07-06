from langchain_groq import ChatGroq
from config.settings import settings
from core.enums import LLMProvider
from core.logger import get_logger
from services.llm.base import BaseLLM

logger = get_logger(__name__)

class GroqProvider(BaseLLM):
    def __init__(self):
        super().__init__(provider=LLMProvider.GROQ, model=settings.llm_model)
        logger.info(f"Initializing Groq model: {self.model}")
        self.client = ChatGroq(model=self.model, api_key=settings.groq_api_key)

    def invoke(self, prompt):
        logger.info(f"Sending prompt to groq.")
        response = self.client.invoke(prompt)
        logger.info("Response received from groq.")
        return response.content

