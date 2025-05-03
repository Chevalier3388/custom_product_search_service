# services/__init__.py

from .redis_service import get_product_from_cache, save_product_to_cache
from .kafka_service import send_product_request_to_kafka
