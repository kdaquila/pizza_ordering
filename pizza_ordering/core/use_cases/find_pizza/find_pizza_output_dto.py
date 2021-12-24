from typing import List
from pizza_ordering.core.entities.pizza import BasePizza


class FindPizzaOutputDTO:
    def __init__(self, pizzas: List[BasePizza]):
        self.pizzas = pizzas
