from application.pizza_repo.abstract_pizza_order_repo import AbstractPizzaRepo
from domain.entities.pizza.base_pizza import BasePizza
from domain.value_objects import PizzaId


class InMemoryPizzaRepo(AbstractPizzaRepo):
    def __init__(self):
        self.orders: [BasePizza] = []

    def get(self, pizza_id: PizzaId) -> BasePizza:
        return next(order for order in self.orders if order.pizza_id == pizza_id)

    def save(self, order: BasePizza) -> None:
        self.orders.append(order)

