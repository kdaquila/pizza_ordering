from uuid import UUID

from pizza_ordering.core.exceptions import PizzaNotFound
from . import AbstractPizzaRepo
from pizza_ordering.core.entities.pizza import BasePizza
from typing import List


class InMemoryPizzaRepo(AbstractPizzaRepo):
    def __init__(self):
        self.pizzas: list = []

    def get(self, pizza_id: UUID) -> BasePizza:
        try:
            return next(pizza for pizza in self.pizzas if pizza.pizza_id == pizza_id)
        except StopIteration:
            raise PizzaNotFound("Invalid pizza id")

    def get_all(self) -> List[BasePizza]:
        return self.pizzas

    def update_one(self, pizza: BasePizza) -> None:
        pizza_index = next(index for (index, p) in enumerate(self.pizzas) if p.pizza_id == pizza.pizza_id)
        self.pizzas[pizza_index] = pizza

    def insert_one(self, pizza: BasePizza) -> None:
        self.pizzas.append(pizza)


