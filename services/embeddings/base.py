from abc import ABC, abstractmethod
from typing import Any



class BaseEmbedding(ABC):
    @abstractmethod
    def get_embedding_model(self) -> Any:
        """Return the configured embedding model."""
        raise NotImplementedError