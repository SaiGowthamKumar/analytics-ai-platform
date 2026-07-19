"""Typed technical configuration."""

from functools import lru_cache

from pydantic import Field
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
    
    # Database configuration
    database_url: str = ""
    db_pool_size: int = Field(default=10, ge=1, le=100)
    db_max_overflow: int = Field(default=20, ge=0, le=100)
    db_pool_timeout: int = Field(default=30, ge=1, le=300)
    db_pool_recycle: int = Field(default=3600, ge=-1, le=86400)
    db_echo: bool = False


@lru_cache
def get_settings() -> Settings:
    """Return the process-wide immutable settings instance."""
    return Settings()
