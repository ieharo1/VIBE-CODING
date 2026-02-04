from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Load settings from a .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Database
    DATABASE_URL: str

    # Redis
    REDIS_URL: str

    # API Settings
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Application Settings
    DEBUG: bool = False


settings = Settings()
