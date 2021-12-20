import abc

from src.domain.value_objects.pizza_id import PizzaId


class AbstractPizzaIdGenerator(abc.ABC):
    @abc.abstractmethod
    def create_new_id(self) -> PizzaId:
        pass
