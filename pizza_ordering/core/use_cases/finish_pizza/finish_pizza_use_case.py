from uuid import UUID

from injector import inject

from pizza_ordering.core.exceptions import PizzaNotCooking
from pizza_ordering.core.pizza_repo import AbstractPizzaRepo
from pizza_ordering.infrastructure.clock import AbstractClock


class FinishPizzaUseCase:
    @inject
    def __init__(self, pizza_repo: AbstractPizzaRepo, clock: AbstractClock) -> None:
        self.clock = clock
        self.pizza_repo = pizza_repo

    def execute(self, pizza_id: UUID) -> None:
        pizza = self.pizza_repo.get(pizza_id)
        if pizza.is_cooking is False:
            raise PizzaNotCooking("This pizza is not currently being cooked")
        pizza.finish_cooking_at(self.clock.current_local_time())
        self.pizza_repo.update_one(pizza)
