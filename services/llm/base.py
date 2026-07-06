from abc import ABC, abstractmethod
from typing import Any

class BaseLLM(ABC):
    "Abstract base class for all LLM providers."

    def __init__(self, provider: str, model: str,):
        self.provider = provider
        self.model = model
    @abstractmethod
    def invoke(self, prompt: Any) -> str:
        raise NotImplementedError

