from pydantic_settings import BaseSettings, SettingsConfigDict
from core.enums import LLMProvider, SplitterStrategy, EmbeddingProvider


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )
    llm_provider: LLMProvider
    llm_model: str
    embedding_provider: EmbeddingProvider
    embedding_model: str
    groq_api_key: str
    chunk_size: int
    chunk_overlap: int
    text_splitter: SplitterStrategy
    log_level: str = "INFO"

settings = Settings()