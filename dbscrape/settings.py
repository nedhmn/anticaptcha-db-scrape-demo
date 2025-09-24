from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    ANTICAPTCHA_API_KEY: str = Field(...)
    SITE_KEY: str = Field(...)


settings = Settings()
