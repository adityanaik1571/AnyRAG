from abc import ABC, abstractmethod
from typing import Any

from core.enums import LLMProvider


class BaseLLM(ABC):
    "Abstract base class for all LLM providers."

    def __init__(self, provider: LLMProvider, model: str,):
        self.provider = provider
        self.model = model
    @abstractmethod
    def invoke(self, prompt: Any) -> str:
        raise NotImplementedError

