from uuid import UUID
import time
from injector import inject

from pizza_ordering import config
from pizza_ordering.core.pizza_repo import AbstractPizzaRepo
from pizza_ordering.core.exceptions import PizzaNotCooking, CannotCancelPizza
from pizza_ordering.infrastructure.clock import AbstractClock


class CancelPizzaUseCase:
    @inject
    def __init__(self, pizza_repo: AbstractPizzaRepo, clock: AbstractClock) -> None:
        self.clock = clock
        self.pizza_repo = pizza_repo

    def execute(self, pizza_id: UUID) -> None:
        current_time = self.clock.current_local_time()
        pizza = self.pizza_repo.get(pizza_id)
        elapsed_time = (current_time - pizza.start_time).total_seconds()
        cancel_order_interval_sec = config.cancel_order_interval_sec
        if pizza.is_cooking is False:
            raise PizzaNotCooking("This pizza is not currently being cooked")
        if elapsed_time > cancel_order_interval_sec:
            raise CannotCancelPizza("This pizza can no longer be cancelled")
        pizza.stop_cooking_at(current_time)
        self.pizza_repo.update_one(pizza)
