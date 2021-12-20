from src.application.clock.abstract_clock import AbstractClock
from src.application.pizza_repo.abstract_pizza_repo import AbstractPizzaRepo
from src.domain.exceptions import CannotCancelPizza
from src.application.pizza_use_cases.cancel_pizza.cancel_pizza_input_dto import CancelPizzaInputDTO
import config


class CancelPizzaUseCase:
    def __init__(self, pizza_repo: AbstractPizzaRepo, clock: AbstractClock) -> None:
        self.clock = clock
        self.pizza_repo = pizza_repo

    def execute(self, input_dto: CancelPizzaInputDTO) -> None:
        current_time = self.clock.current_unix_time_sec()
        pizza_order = self.pizza_repo.get(input_dto.pizza_id)
        start_time = pizza_order.start_time
        elapsed_time = current_time - start_time
        if elapsed_time < config.cancel_order_interval_sec:
            pizza_order.stop_cooking_at(current_time)
            self.pizza_repo.save(pizza_order)
        else:
            raise CannotCancelPizza()
