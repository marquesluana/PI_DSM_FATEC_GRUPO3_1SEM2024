from django.urls import path
from .views import add_product, list_products ,register

urlpatterns = [
    path('register/', register, name='register'),
    # path('food_items/', name='list_food_items'),
    # path('add_food_item/', name='add_food_item'),
    path('add_product/', add_product, name='add_product'),
    path('list_products/', list_products, name='list_products'),
]
