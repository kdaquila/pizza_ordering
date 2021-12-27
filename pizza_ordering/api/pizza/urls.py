from django.urls import path
from pizza_ordering.api.pizza.pizza_controllers import FinishPizzaController, CancelPizzaController, PizzaController

urlpatterns = [
    path('pizza', PizzaController.as_view()),
    path('pizza/<str:pizza_id>/cancel', CancelPizzaController.as_view()),
    path('pizza/<str:pizza_id>/finish', FinishPizzaController.as_view()),
]
