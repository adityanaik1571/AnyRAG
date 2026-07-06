from config.settings import settings
from services.llm.base import BaseLLM
from core.logger import get_logger

logger = get_logger(__name__)
class LLMFactory:
    @staticmethod
    def create() -> BaseLLM:
        provider = settings.llm_provider.lower()
        logger.info(f"Creating LLM provider: {provider}")
        raise NotImplementedError(f"LLM Provider {provider} is not implemented yet.")