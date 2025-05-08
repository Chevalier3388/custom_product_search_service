# product/views_redis.py

from django.shortcuts import render

from src.utils.kafka_service.kafka_service import send_product_request_to_kafka
from src.utils.redis_service import get_product_from_cache
from src.utils.settings import settings



def get_product(request):
    try:
        if request.method == "GET":
            product_name = request.GET.get("product_name")
            if not product_name:
                # Если product_name не передано
                return render(
                    request,
                    "product/search_product.html",
                    {"message": "Введите имя продукта для поиска."},
                )

            # Пытаемся получить товар из кэша Redis
            product_data = get_product_from_cache(product_name)
            if product_data:
                # Если продукт найден в Redis
                return render(
                    request,
                    "product/search_product.html",
                    {"product": product_data, "product_name": product_name},
                )

            send_product_request_to_kafka(
                settings.KAFKA_PRODUCT_REQUESTS_TOPIC, {"product_name": product_name}
            )
            return render(
                request,
                "product/search_product.html",
                {
                    "message": "Продукт в обработке. Попробуйте снова через несколько секунд.",
                    "product_name": product_name,
                },
            )

    except Exception as e:
        # Обработка ошибок, если что-то пошло не так
        return render(
            request,
            "product/search_product.html",
            {"message": f"Произошла ошибка: {str(e)}"},
        )
