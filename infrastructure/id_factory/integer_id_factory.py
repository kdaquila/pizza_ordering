from infrastructure.id_factory import AbstractIdFactory
from core.pizza_id import PizzaId


class IntegerIdFactory(AbstractIdFactory):
    def __init__(self):
        super().__init__()
        self.current_id = 0

    def create_new_id(self) -> PizzaId:
        self.current_id += 1
        return self.current_id
