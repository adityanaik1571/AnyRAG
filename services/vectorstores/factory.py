from services.vectorstores.providers.chroma_vectorstore_provider import ChromaVectorStoreProvider
from core.logger import get_logger
from core.enums import VectorStoreProvider
from config.settings import settings

VECTOR_STORE_REGISTRY = {
    VectorStoreProvider.CHROMA: ChromaVectorStoreProvider,
}

logger = get_logger(__name__)

class VectorStoreFactory:
    @staticmethod
    def create(embedding_model):
        logger.info(f"Creating vector store provider: {settings.vector_store_provider.value}")
        vector_class = VECTOR_STORE_REGISTRY.get(settings.vector_store_provider.value)
        if vector_class is None:
            raise NotImplementedError(f"Vector store provider {settings.vector_store_provider.value} not implemented yet")
        return vector_class(embedding_model)
