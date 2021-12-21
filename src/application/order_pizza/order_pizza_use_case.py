from injector import inject

from application.clock import AbstractClock
from application.order_pizza.order_pizza_input_dto import OrderPizzaInputDTO
from application.order_pizza.order_pizza_output_dto import OrderPizzaOutputDTO
from application.pizza_factory import AbstractPizzaFactory
from application.pizza_repo import AbstractPizzaRepo


class OrderPizzaUseCase:
    @inject
    def __init__(self, pizza_repo: AbstractPizzaRepo,
                 clock: AbstractClock,
                 pizza_factory: AbstractPizzaFactory) -> None:
        self.pizza_repo = pizza_repo
        self.clock = clock
        self.pizza_factory = pizza_factory

    def execute(self, input_dto: OrderPizzaInputDTO) -> OrderPizzaOutputDTO:
        current_time = self.clock.current_unix_time_sec()
        new_pizza = self.pizza_factory.build(input_dto.pizza_type)
        new_pizza.start_cooking_at(current_time)
        self.pizza_repo.insert_one(new_pizza)
        return OrderPizzaOutputDTO("success", "", new_pizza.pizza_id)