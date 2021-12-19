import abc

from domain.value_objects import PizzaId


class AbstractPizzaIdGenerator(abc.ABC):
    @abc.abstractmethod
    def create_new_id(self) -> PizzaId:
        pass
