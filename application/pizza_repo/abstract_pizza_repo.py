import abc
from domain.entities.pizza.base_pizza import BasePizza
from domain.value_objects import PizzaId


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
