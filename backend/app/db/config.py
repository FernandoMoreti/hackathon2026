from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Hackathon 2026 API"
    database_url: str = "postgresql+psycopg://root:root@localhost:5433/hack"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()