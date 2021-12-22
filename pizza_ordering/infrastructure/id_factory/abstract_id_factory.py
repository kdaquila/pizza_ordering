import abc

from pizza_ordering.core.pizza_id import PizzaId


class AbstractIdFactory(abc.ABC):
    @abc.abstractmethod
    def create_new_id(self) -> PizzaId:
        pass
