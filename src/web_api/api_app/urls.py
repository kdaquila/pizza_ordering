from django.urls import path
from .pizza_controller import PizzaController

urlpatterns = [
    path('pizza', PizzaController.as_view(), name='index'),
    path('pizza/<int:pizza_id_generator>', PizzaController.as_view(), name='index'),
]
