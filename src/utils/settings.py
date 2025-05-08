from pydantic_settings import BaseSettings

ENV_FILENAME = '../.env'


class Settings(BaseSettings):
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    KAFKA_BOOTSTRAP_SERVERS: str = "kafka:9092"

    class Config:
        env_file = ENV_FILENAME
        env_file_encoding = 'utf-8'


settings = Settings()
