# Modern configuration compatible with Pydantic v2

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Real-Time Fraud Detection API"
    VERSION: str = "1.0.0"


settings = Settings()
