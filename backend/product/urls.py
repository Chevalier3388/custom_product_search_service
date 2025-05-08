
from django.urls import path
from . import views_html
from . import views_redis


urlpatterns = [
    path("", views_html.home, name="home"),
    path("search/", views_html.search_product, name="search_product"),
    path("search/", views_redis.get_product, name="get_product"),
]

