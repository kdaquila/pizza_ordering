from application.order_repo.pizza_order_repo import PizzaOrderRepo
from domain.entities.pizza_order.base_pizza_order import BasePizzaOrder
from domain.value_objects import OrderId


class InMemoryPizzaRepo(PizzaOrderRepo):
    def __init__(self):
        self.orders: [BasePizzaOrder] = []

    def get(self, order_id: OrderId) -> BasePizzaOrder:
        return next(order for order in self.orders if order.order_id == order_id)

    def save(self, order: BasePizzaOrder) -> None:
        self.orders.append(order)

