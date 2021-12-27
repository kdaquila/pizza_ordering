from uuid import UUID
from injector import inject

from pizza_ordering import config
from pizza_ordering.core.pizza_repo import AbstractPizzaRepo
from pizza_ordering.core.exceptions import PizzaNotCooking, CannotCancelPizza, PizzaNotFound
from pizza_ordering.infrastructure.clock import AbstractClock


class DeletePizzaUseCase:
    @inject
    def __init__(self, pizza_repo: AbstractPizzaRepo) -> None:
        self.pizza_repo = pizza_repo

    def execute(self) -> None:
        pizzas = self.pizza_repo.get_all()
        if len(pizzas) == 0:
            raise PizzaNotFound("There were no pizzas orders found")
        self.pizza_repo.delete_all()
