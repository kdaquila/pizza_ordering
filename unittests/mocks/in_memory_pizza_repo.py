from application.pizza_repo.abstract_pizza_repo import AbstractPizzaRepo
from domain.entities.pizza.base_pizza import BasePizza
from domain.value_objects import PizzaId


class InMemoryPizzaRepo(AbstractPizzaRepo):
    def __init__(self):
        self.pizzas: list = []

    def get(self, pizza_id: PizzaId) -> BasePizza:
        return next(pizza for pizza in self.pizzas if pizza.pizza_id == pizza_id)

    def get_all(self) -> list:
        return self.pizzas

    def save(self, pizza: BasePizza) -> None:
        self.pizzas.append(pizza)
