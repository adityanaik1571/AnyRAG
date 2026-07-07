from config.settings import settings
from services.embeddings.base import BaseEmbedding
from core.enums import EmbeddingProvider
from core.logger import get_logger
from services.embeddings.providers.huggingface_embeddings_provider import HuggingFaceEmbeddingsProvider

logger = get_logger(__name__)

EMBEDDING_REGISTRY = {
    EmbeddingProvider.HUGGINGFACE: HuggingFaceEmbeddingsProvider,
}

class EmbeddingFactory:
    @staticmethod
    def create() -> BaseEmbedding:
        logger.info(f'Creating embedding provider: {settings.embedding_provider.value}')
        embedding_class = EMBEDDING_REGISTRY.get(settings.embedding_provider)
        if embedding_class is None:
            raise NotImplementedError(f"The embedding provider {settings.embedding_provider} is not implemented yet")
        return embedding_class()



