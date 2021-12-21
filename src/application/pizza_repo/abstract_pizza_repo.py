import abc

from domain.pizza.base_pizza import BasePizza
from domain.pizza_id import PizzaId


class AbstractPizzaRepo(abc.ABC):
    @abc.abstractmethod
    def get(self, pizza_id: PizzaId) -> BasePizza:
        pass

    @abc.abstractmethod
    def get_all(self) -> BasePizza:
        pass

    @abc.abstractmethod
    def update_one(self, pizza: BasePizza) -> None:
        pass

    @abc.abstractmethod
    def insert_one(self, pizza: BasePizza) -> None:
        pass
