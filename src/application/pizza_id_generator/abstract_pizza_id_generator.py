import abc

from domain.pizza_id.pizza_id import PizzaId


class AbstractPizzaIdGenerator(abc.ABC):
    @abc.abstractmethod
    def create_new_id(self) -> PizzaId:
        pass
