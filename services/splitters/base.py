from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class BaseSplitter(ABC):
    """Abstract base class for all document splitters."""
    @abstractmethod
    def split(self, documents: List[Document]) -> List[Document]:
        """Split documents into smaller chunks."""
        raise NotImplementedError("Split not implemented yet.")
