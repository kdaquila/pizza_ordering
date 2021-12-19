from application.pizza_id.abstract_pizza_id_generator import AbstractPizzaIdGenerator
from domain.value_objects import PizzaId


class IntegerPizzaIdGenerator(AbstractPizzaIdGenerator):
    def __init__(self):
        super().__init__()
        self.current_id = 0

    def create_new_id(self) -> PizzaId:
        self.current_id += 1
        return self.current_id
