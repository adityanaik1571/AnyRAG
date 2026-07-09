from abc import ABC, abstractmethod
from services.reasoning.models import UserInstruction

class BaseInstructionInterpreter(ABC):
    """Base class for all instruction interpreters."""
    @abstractmethod
    def interpret(self, user_input: str) -> UserInstruction:
        """Convert natural language into a structured UserInstruction."""
        raise NotImplementedError