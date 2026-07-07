from enum import Enum

class LLMProvider(str, Enum):
    GROQ="groq"

class SplitterStrategy(Enum):
    RECURSIVE = "recursive"