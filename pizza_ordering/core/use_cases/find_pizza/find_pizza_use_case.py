from typing import List

from injector import inject

from pizza_ordering.core.output_dto.pizza import Pizza as PizzaDTO
from pizza_ordering.core.pizza_repo import AbstractPizzaRepo
from pizza_ordering.infrastructure.clock import AbstractClock
from pizza_ordering.infrastructure.time_convert import TimeConverter


class FindPizzaUseCase:
    @inject
    def __init__(self, pizza_repo: AbstractPizzaRepo, clock: AbstractClock, time_converter: TimeConverter):
        self.pizza_repo = pizza_repo
        self.clock = clock
        self.time_converter = time_converter

    def execute(self) -> List[PizzaDTO]:
        pizzas = self.pizza_repo.get_all()
        output = []
        for pizza in pizzas:
            output.append(PizzaDTO(pizza_id=str(pizza.pizza_id), name=pizza.name, description=pizza.description,
                                   status=pizza.status, start_time=pizza.start_time, stop_time=pizza.stop_time))
        return output
