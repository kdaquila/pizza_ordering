import abc
from src.domain.entities.pizza.base_pizza import BasePizza
from src.domain.value_objects.pizza_id import PizzaId


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
