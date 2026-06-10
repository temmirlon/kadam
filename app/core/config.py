from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Strava AI Coach"
    app_env: str = "local"
    debug: bool = True

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()