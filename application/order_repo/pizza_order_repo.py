import abc
from domain.entities.pizza_order.base_pizza_order import BasePizzaOrder
from domain.value_objects import OrderId


class PizzaOrderRepo(abc.ABC):
    @abc.abstractmethod
    def get(self, order_id: OrderId) -> BasePizzaOrder:
        pass

    @abc.abstractmethod
    def save(self, order: BasePizzaOrder) -> None:
        pass
