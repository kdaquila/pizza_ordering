from injector import inject

from application.clock import AbstractClock
from application.pizza_repo import AbstractPizzaRepo
from application.find_pizza.find_pizza_output_dto import FindPizzaOutputDTO


class FindPizzaUseCase:
    @inject
    def __init__(self, pizza_repo: AbstractPizzaRepo, clock: AbstractClock):
        self.pizza_repo = pizza_repo
        self.clock = clock

    def execute(self) -> FindPizzaOutputDTO:
        return FindPizzaOutputDTO(self.pizza_repo.get_all(), "success", "")