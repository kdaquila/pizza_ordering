import abc
from uuid import UUID

from pizza_ordering.core.entities.pizza import BasePizza
from typing import List


class AbstractPizzaRepo(abc.ABC):
    @abc.abstractmethod
    def get(self, pizza_id: UUID) -> BasePizza:
        pass

    @abc.abstractmethod
    def get_all(self) -> List[BasePizza]:
        pass

    @abc.abstractmethod
    def update_one(self, pizza: BasePizza) -> None:
        pass

    @abc.abstractmethod
    def insert_one(self, pizza: BasePizza) -> None:
        pass
