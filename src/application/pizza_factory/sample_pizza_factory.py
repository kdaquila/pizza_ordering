from injector import inject

from application.pizza_factory import AbstractPizzaFactory
from application.pizza_id_generator import AbstractPizzaIdGenerator
from domain.exceptions import InvalidPizzaType
from domain.pizza import CheesePizza, PepperoniPizza, SausagePizza, BasePizza


class SamplePizzaFactory(AbstractPizzaFactory):
    @inject
    def __init__(self, pizza_id_factory: AbstractPizzaIdGenerator):
        self.pizza_mapping = {"cheese": CheesePizza, "pepperoni": PepperoniPizza, "sausage": SausagePizza}
        self.pizza_id_factory = pizza_id_factory

    def build(self, pizza_type: str) -> BasePizza:
        new_pizza_id = self.pizza_id_factory.create_new_id()
        new_pizza = self.pizza_mapping[pizza_type](new_pizza_id)
        return new_pizza

