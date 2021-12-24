from django.urls import path
from pizza_ordering.api.pizza.pizza_controller import PizzaController

urlpatterns = [
    path('pizza', PizzaController.as_view(), name='index'),
    path('pizza/<int:pizza_id>', PizzaController.as_view(), name='index'),
]
