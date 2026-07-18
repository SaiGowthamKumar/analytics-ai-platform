"""Typed technical configuration."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings with safe local defaults."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="APP_",
        extra="ignore",
    )

    service_name: str = "ai-analytics-platform"
    service_version: str = "0.1.0"
    environment: str = "development"
    api_prefix: str = "/api/v1"
    docs_enabled: bool = True
    log_level: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    """Return the process-wide immutable settings instance."""
    return Settings()
