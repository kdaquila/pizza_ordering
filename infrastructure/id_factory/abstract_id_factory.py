import abc

from core.pizza_id import PizzaId


class AbstractIdFactory(abc.ABC):
    @abc.abstractmethod
    def create_new_id(self) -> PizzaId:
        pass
