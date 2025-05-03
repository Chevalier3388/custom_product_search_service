
from django.urls import path
from . import views_html



urlpatterns = [
    path("", views_html.home, name="home"),
    path("search/", views_html.search_product, name="search_product"),
]

