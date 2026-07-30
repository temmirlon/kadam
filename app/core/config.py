from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

class Settings(BaseSettings):
    app_name: str = "Strava AI Coach"
    app_env: str = "local"
    debug: bool = True
    ai_provider: Literal["fake"] = "fake"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()