from injector import inject

import config
from application.cancel_pizza.cancel_pizza_input_dto import CancelPizzaInputDTO
from application.cancel_pizza.cancel_pizza_output_dto import CancelPizzaOutputDTO
from application.clock import AbstractClock
from application.pizza_repo import AbstractPizzaRepo
from domain.exceptions import CannotCancelPizza, PizzaNotFound


class CancelPizzaUseCase:
    @inject
    def __init__(self, pizza_repo: AbstractPizzaRepo, clock: AbstractClock) -> None:
        self.clock = clock
        self.pizza_repo = pizza_repo

    def execute(self, input_dto: CancelPizzaInputDTO) -> CancelPizzaOutputDTO:
        current_time = self.clock.current_unix_time_sec()
        try:
            pizza = self.pizza_repo.get(input_dto.pizza_id)
        except PizzaNotFound:
            return CancelPizzaOutputDTO(status="fail", message=f"Pizza {input_dto.pizza_id} could not be found")
        start_time = pizza.start_time
        elapsed_time = current_time - start_time
        cancel_order_interval_sec = config.cancel_order_interval_sec
        if pizza.is_cooking is False:
            return CancelPizzaOutputDTO(status="fail", message=f"Pizza {input_dto.pizza_id} is already stopped")
        if elapsed_time > cancel_order_interval_sec:
            return CancelPizzaOutputDTO(status="fail", message=f"Pizza {input_dto.pizza_id} cannot be stopped")

        pizza.stop_cooking_at(current_time)
        self.pizza_repo.update_one(pizza)
        return CancelPizzaOutputDTO(status="success", message=f"Pizza {input_dto.pizza_id} was stopped")