from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )
    llm_provider: str
    llm_model: str
    embedding_provider: str
    embedding_model: str
    groq_api_key: str
    log_level: str = "INFO"

settings = Settings()