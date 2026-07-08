from core.logger import get_logger
from services.vectorstores.base import BaseVectorStore
from config.settings import settings
from langchain_chroma import Chroma

logger = get_logger(__name__)

class ChromaVectorStoreProvider(BaseVectorStore):
    def __init__(self, embedding_model):
        logger.info(f'Initializing chroma vector store: {settings.chroma_collection_name}')
        self.embedding_model = embedding_model
        self.vector_store = Chroma(
            collection_name=settings.chroma_collection_name,
            embedding_function = self.embedding_model,
            persist_directory=settings.chroma_persist_directory
        )
    def store(self, documents):
        logger.info(f"Storing {len(documents)} documents in ChromaDB")
        self.vector_store.add_documents(documents)

    def retrieve(self, query):
        logger.info(f"Searching VectorStore for {query}")
        return self.vector_store.similarity_search(query=query, k=settings.retrieval_top_k)