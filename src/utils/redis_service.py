import redis
import logging

from .settings import settings

# Логирование для ошибок
logging.basicConfig(level=logging.INFO)

# Здесь задаём настройки Redis напрямую в коде
# todo: Подтягивать из settings.REDIS_HOST, etc

REDIS_HOST = settings.REDIS_HOST
REDIS_PORT = settings.REDIS_PORT
REDIS_DB = settings.REDIS_DB

# Настроим Redis с обработкой ошибок
try:
    redis_client = redis.StrictRedis(
        host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True
    )
    logging.info("Подключение к Redis успешно установлено")
except Exception as e:
    logging.error(f"Ошибка подключения к Redis: {e}")
    raise


def get_product_from_cache(product_name):
    """
    Получаем данные продукта из Redis
    """
    try:
        data = redis_client.get(f"product:{product_name}")
        if data:
            logging.info(f"Данные для продукта {product_name} получены из Redis")
        else:
            logging.info(f"Данные для продукта {product_name} не найдены в Redis")
        return data
    except Exception as e:
        logging.error(f"Ошибка при получении данных из Redis: {e}")
        raise


def save_product_to_cache(product_name, data, ttl=3600):
    """
    Сохраняем данные продукта в Redis
    """
    try:
        redis_client.setex(f"product:{product_name}", ttl, data)
        logging.info(f"Данные для продукта {product_name} сохранены в Redis")
    except Exception as e:
        logging.error(f"Ошибка при сохранении данных в Redis: {e}")
        raise
