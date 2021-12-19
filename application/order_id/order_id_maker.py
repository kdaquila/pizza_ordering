import abc

from domain.value_objects import OrderId


class OrderIdMaker(abc.ABC):
    @abc.abstractmethod
    def create_new_id(self) -> OrderId:
        pass
