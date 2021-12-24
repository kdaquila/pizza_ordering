from injector import inject

from pizza_ordering.core.exceptions import InvalidPizzaType
from . import AbstractPizzaFactory
from pizza_ordering.core.entities.pizza import BasePizza
from pizza_ordering.infrastructure.id_factory import AbstractIdFactory


class SamplePizzaFactory(AbstractPizzaFactory):
    @inject
    def __init__(self, pizza_id_factory: AbstractIdFactory):
        self.pizza_mapping = {
            "cheese": {
                "name": "cheese",
                "description": "Pizza crust with only Mozarella cheese over tomato sauce"},
            "pepperoni": {
                "name": "pepperoni",
                "description": "Pizza crust with mozarella cheese and pepperoni over tomato sauce"},
            "sausage": {
                "name": "sausage",
                "description": "Pizza crust with mozarella cheese and sausage over tomato sauce"}
        }
        self.pizza_id_factory = pizza_id_factory

    def build(self, pizza_type: str) -> BasePizza:
        new_pizza_id = self.pizza_id_factory.create_new_id()

        try:
            pizza_info = self.pizza_mapping[pizza_type]
            new_pizza = BasePizza(new_pizza_id, pizza_info["name"], pizza_info["description"])
        except KeyError:
            raise InvalidPizzaType("Pizza type is not valid")

        return new_pizza
