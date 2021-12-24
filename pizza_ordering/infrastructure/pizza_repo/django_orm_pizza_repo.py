from typing import List
from uuid import UUID

from injector import inject

from pizza.models import Pizza
from pizza_ordering.core.entities.pizza import BasePizza
from pizza_ordering.core.exceptions import PizzaNotFound
from pizza_ordering.core.pizza_repo import AbstractPizzaRepo
from pizza_ordering.infrastructure.time_convert import TimeConverter


class DjangoORMPizzaRepo(AbstractPizzaRepo):
    @inject
    def __init__(self, time_converter: TimeConverter):
        self.time_converter = time_converter

    def get(self, pizza_id: UUID) -> BasePizza:
        try:
            pizza = Pizza.objects.get(id=pizza_id)
            return BasePizza(pizza_id=pizza.id, name=pizza.name, description=pizza.description,
                             start_time=pizza.start_time,
                             stop_time=pizza.stop_time)
        except Pizza.DoesNotExist:
            raise PizzaNotFound("Could not find the pizza")

    def get_all(self) -> List[BasePizza]:
        pizzas = Pizza.objects.all()
        output = []
        for pizza in pizzas:
            output.append(
                BasePizza(pizza_id=pizza.id, name=pizza.name, description=pizza.description,
                          start_time=pizza.start_time,
                          stop_time=pizza.stop_time))
        return output

    def update_one(self, pizza: BasePizza) -> None:
        stored_pizza = Pizza.objects.get(id=pizza.pizza_id)
        stored_pizza.name = pizza.name
        stored_pizza.description = pizza.description
        stored_pizza.start_time = pizza.start_time
        stored_pizza.stop_time = pizza.stop_time
        stored_pizza.save()

    def insert_one(self, pizza: BasePizza) -> None:
        new_pizza = Pizza(
            id=pizza.pizza_id,
            name=pizza.name,
            description=pizza.description,
            start_time=pizza.start_time,
            stop_time=pizza.stop_time)
        new_pizza.save()
