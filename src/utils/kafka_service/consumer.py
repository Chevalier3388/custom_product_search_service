import json  # Для сериализации и десериализации данных в JSON
from time import sleep  # Для имитации задержки обработки


# Импортируем функцию сохранения данных в Redis
from utils.redis_service import save_product_to_cache

# Импортируем функцию получения Kafka consumer'а
from utils.kafka_service.kafka_service import get_consumer


# Функция обработки одного Kafka-сообщения
def process_message(message):
    data = message.value  # Получаем данные сообщения (предполагается JSON)
    product_name = data.get("product_name")  # Извлекаем имя продукта

    if not product_name:
        print("⚠️ Пропущено сообщение без 'product_name'")
        return  # Пропускаем сообщение, если нет ключа 'product_name'

    print(f"📥 Обработка: {product_name}")
    sleep(2)  # Имитация задержки (например, обращение к API или БД)

    # Создаём пример данных продукта
    product_data = {
        "name": product_name,
        "price": "99.99",
        "description": f"{product_name} — пример описания",
    }

    try:
        # Сохраняем данные в Redis с использованием сервиса
        save_product_to_cache(product_name, json.dumps(product_data))
        print(f"✅ Сохранено в Redis: {product_name}")
    except Exception as e:
        # Обработка ошибок при сохранении
        print(f"❌ Ошибка при сохранении в Redis: {e}")


# Основная точка входа
def launch_consumer():
    consumer = get_consumer()  # Получаем Kafka consumer
    print("🎧 Запуск консюмера...")  # Сообщаем о запуске

    # Бесконечно слушаем Kafka-топик
    for message in consumer:
        try:
            process_message(message)  # Обрабатываем каждое сообщение
        except Exception as e:
            # Общий обработчик ошибок на случай проблем при обработке
            print(f"❌ Ошибка при обработке сообщения: {e}")
