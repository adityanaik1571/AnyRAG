from config.settings import settings
from core.logger import get_logger
from services.embeddings.base import BaseEmbedding
from langchain_huggingface import HuggingFaceEmbeddings


logger = get_logger(__name__)

class HuggingFaceEmbeddingsProvider(BaseEmbedding):
    def __init__(self):
        embedding_model_name = settings.embedding_model
        logger.info(f"Initializing Huggingface embedding model: {embedding_model_name}")
        self.embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)

    def get_embedding_model(self) -> HuggingFaceEmbeddings:
        return self.embedding_model

