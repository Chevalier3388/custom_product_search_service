from kafka import KafkaProducer, KafkaConsumer
import json
import logging

# Логирование для ошибок подключения и отправки/получения сообщений
logging.basicConfig(level=logging.INFO)

# Здесь задаём настройки Kafka напрямую в коде
# KAFKA_BOOTSTRAP_SERVERS = [
#     'kafka:9092',
#     "localhost:9092",
#     "172.26.0.4:9092"
# ]
KAFKA_PRODUCT_REQUESTS_TOPIC = 'product_requests'  # Тема для consumer

def get_producer():
    """
    Получаем Kafka producer с необходимыми параметрами
    """
    try:
        producer = KafkaProducer(
            bootstrap_servers="kafka:9092",
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        logging.info("Kafka Producer создан успешно")
        return producer
    except Exception as e:
        logging.error(f"Ошибка при создании Kafka Producer: {e}")
        raise

def get_consumer():
    """
    Получаем Kafka consumer с необходимыми параметрами
    """
    try:
        consumer = KafkaConsumer(
            KAFKA_PRODUCT_REQUESTS_TOPIC,
            bootstrap_servers="kafka:9092",
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='product-consumers',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        logging.info("Kafka Consumer создан успешно")
        return consumer
    except Exception as e:
        logging.error(f"Ошибка при создании Kafka Consumer: {e}")
        raise

def send_product_request_to_kafka(topic, message):
    """
    Отправляем сообщение в Kafka
    """
    try:
        producer = get_producer()
        producer.send(topic, message)
        producer.flush()
        producer.close()
        logging.info(f"Сообщение отправлено в Kafka, тема: {topic}")
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения в Kafka: {e}")
