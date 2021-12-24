from uuid import uuid4

from pizza_ordering.core.pizza_id import PizzaId
from pizza_ordering.infrastructure.id_factory import AbstractIdFactory


class UUIDFactory(AbstractIdFactory):
    def create_new_id(self) -> PizzaId:
        return uuid4()
