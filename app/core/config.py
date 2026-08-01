from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Strava AI Coach"
    app_env: str = "local"
    debug: bool = True
    ai_provider: Literal["fake"] = "fake"
    

    strava_client_id: str = ""
    strava_client_secret: str = ""
    strava_redirect_uri: str = ""


    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()