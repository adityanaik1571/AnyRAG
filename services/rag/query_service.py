from services.embeddings.factory import EmbeddingFactory
from services.vectorstores.factory import VectorStoreFactory
from core.logger import get_logger
from langchain_core.documents import Document

logger = get_logger(__name__)

class QueryService:
    def __init__(self):
        embedding_provider = EmbeddingFactory.create()
        embedding_model = embedding_provider.get_embedding_model()
        self.vector_store = VectorStoreFactory.create(embedding_model=embedding_model)

    def ask(self, question: str) -> list[Document]:
        logger.info(f"Received query: {question}")
        logger.info("Retrieving relevant documents...")
        return self.vector_store.retrieve(question)