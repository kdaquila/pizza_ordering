from injector import inject

from pizza_ordering.infrastructure.clock import AbstractClock
from pizza_ordering.core.pizza_repo import AbstractPizzaRepo
from pizza_ordering.core.use_cases.find_pizza.find_pizza_output_dto import FindPizzaOutputDTO


class FindPizzaUseCase:
    @inject
    def __init__(self, pizza_repo: AbstractPizzaRepo, clock: AbstractClock):
        self.pizza_repo = pizza_repo
        self.clock = clock

    def execute(self) -> FindPizzaOutputDTO:
        try:
            pizzas = self.pizza_repo.get_all()
            return FindPizzaOutputDTO(pizzas, status="success", message="")
        except Exception:
            return FindPizzaOutputDTO(None, status="error", message="Internal server error.")