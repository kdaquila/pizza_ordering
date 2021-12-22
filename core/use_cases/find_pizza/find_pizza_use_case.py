from injector import inject

from infrastructure.clock import AbstractClock
from core.pizza_repo import AbstractPizzaRepo
from core.use_cases.find_pizza.find_pizza_output_dto import FindPizzaOutputDTO


class FindPizzaUseCase:
    @inject
    def __init__(self, pizza_repo: AbstractPizzaRepo, clock: AbstractClock):
        self.pizza_repo = pizza_repo
        self.clock = clock

    def execute(self) -> FindPizzaOutputDTO:
        return FindPizzaOutputDTO(self.pizza_repo.get_all(), "success", "")