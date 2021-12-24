from django.urls import path
from pizza_ordering.api.pizza.pizza_controller import PizzaController

urlpatterns = [
    path('pizza', PizzaController.as_view()),
    path('pizza/<str:pizza_id>', PizzaController.as_view()),
]
