from config.settings import settings
from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class BaseVectorStore(ABC):
    """Abstract base class for all vector stores."""
    @abstractmethod
    def store(self, documents: List[Document]) -> None:
        """Store documents in the vector store."""
        raise NotImplementedError("Vector Store not implemented yet.")
    @abstractmethod
    def retrieve(self, query: str) -> List[Document]:
        """Retrieve the most relevant documents for a query."""
        raise NotImplementedError("Vector Store not implemented yet.")
