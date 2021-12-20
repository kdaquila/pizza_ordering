from application.clock.abstract_clock import AbstractClock
from application.pizza_repo.abstract_pizza_repo import AbstractPizzaRepo
from domain.pizza.base_pizza import BasePizza


class OutputDTO:
    def __init__(self, pizzas: [BasePizza], status: str = "", message: str = ""):
        self.status = status
        self.message = message
        self.data = {"pizzas": pizzas}


class UseCase:
    def __init__(self, pizza_repo: AbstractPizzaRepo, clock: AbstractClock):
        self.pizza_repo = pizza_repo
        self.clock = clock

    def execute(self) -> OutputDTO:
        return OutputDTO(self.pizza_repo.get_all(), "success", "")
