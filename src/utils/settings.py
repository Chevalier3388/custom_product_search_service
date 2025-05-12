from pydantic_settings import BaseSettings

ENV_FILENAME = "../../.env"


class Settings(BaseSettings):
    REDIS_HOST: str = "redis_cache"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    KAFKA_BOOTSTRAP_SERVERS: list = [
        "kafka:9092",
        "localhost:9093",
    ]
    KAFKA_PRODUCT_REQUESTS_TOPIC: str = "product_requests"

    class Config:
        env_file = ENV_FILENAME
        env_file_encoding = "utf-8"


settings = Settings()
