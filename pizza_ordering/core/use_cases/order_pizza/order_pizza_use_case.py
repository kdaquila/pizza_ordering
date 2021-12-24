from injector import inject

from pizza_ordering.infrastructure.clock import AbstractClock
from pizza_ordering.core.output_dto.pizza_id import PizzaId as PizzaIdDTO
from pizza_ordering.core.pizza_factory import AbstractPizzaFactory
from pizza_ordering.core.pizza_repo import AbstractPizzaRepo


class OrderPizzaUseCase:
    @inject
    def __init__(self, pizza_repo: AbstractPizzaRepo,
                 clock: AbstractClock,
                 pizza_factory: AbstractPizzaFactory) -> None:
        self.pizza_repo = pizza_repo
        self.clock = clock
        self.pizza_factory = pizza_factory

    def execute(self, pizza_type: str) -> PizzaIdDTO:
        current_time = self.clock.current_unix_time_sec()
        new_pizza = self.pizza_factory.build(pizza_type)
        new_pizza.start_cooking_at(current_time)
        self.pizza_repo.insert_one(new_pizza)
        return PizzaIdDTO(new_pizza.pizza_id)
