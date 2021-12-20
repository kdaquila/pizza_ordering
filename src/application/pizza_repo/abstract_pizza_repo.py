import abc
from domain.pizza.base_pizza import BasePizza
from domain.pizza_id.pizza_id import PizzaId


class AbstractPizzaRepo(abc.ABC):
    @abc.abstractmethod
    def get(self, order_id: PizzaId) -> BasePizza:
        pass

    @abc.abstractmethod
    def get_all(self) -> BasePizza:
        pass

    @abc.abstractmethod
    def save(self, order: BasePizza) -> None:
        pass
