from utils.kafka_service.consumer import launch_consumer
from utils.settings import settings

if __name__ == "__main__":
    print(settings.REDIS_HOST)
    launch_consumer()
