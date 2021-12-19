from src.application.clock.abstract_clock import AbstractClock
from src.application.pizza_repo.abstract_pizza_repo import AbstractPizzaRepo


class GetPizzaUseCase:
    def __init__(self, pizza_repo: AbstractPizzaRepo, clock: AbstractClock):
        self.pizza_repo = pizza_repo
        self.clock = clock

    def execute(self):
        return self.pizza_repo.get_all()
