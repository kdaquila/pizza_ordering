import config
from application.clock.abstract_clock import AbstractClock
from application.pizza_repo.abstract_pizza_repo import AbstractPizzaRepo
from domain.exceptions import CannotCancelPizza
from domain.pizza_id import PizzaId


class InputDTO:
    def __init__(self, pizza_id: PizzaId) -> None:
        self.pizza_id = pizza_id


class OutputDTO:
    def __init__(self, status: str = "", message: str = ""):
        self.status = status
        self.message = message
        self.data = {}


class UseCase:
    def __init__(self, pizza_repo: AbstractPizzaRepo, clock: AbstractClock) -> None:
        self.clock = clock
        self.pizza_repo = pizza_repo

    def execute(self, input_dto: InputDTO) -> OutputDTO:
        current_time = self.clock.current_unix_time_sec()
        pizza_order = self.pizza_repo.get(input_dto.pizza_id)
        start_time = pizza_order.start_time
        elapsed_time = current_time - start_time
        if elapsed_time > config.cancel_order_interval_sec:
            raise CannotCancelPizza()

        pizza_order.stop_cooking_at(current_time)
        self.pizza_repo.save(pizza_order)
        return OutputDTO("success", f"Pizza {input_dto.pizza_id} was stopped")

