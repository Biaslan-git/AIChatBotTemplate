from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: str = 'Missing value'
    AI_API_TOKEN: str = 'Missing value'
    PROXY_ADDRESS: str = 'Missing value'
    PROXY_PORT: str = 'Missing value'
    PROXY_USER: str = 'Missing value'
    PROXY_PASSWORD: str = 'Missing value'

    class Config:
        env_file = '.env'
        env_file_encoding = "utf-8"

