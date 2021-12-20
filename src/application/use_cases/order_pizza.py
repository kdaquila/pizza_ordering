from application.clock.abstract_clock import AbstractClock
from application.pizza_id_generator.abstract_pizza_id_generator import AbstractPizzaIdGenerator
from application.pizza_repo.abstract_pizza_repo import AbstractPizzaRepo
from domain.exceptions import InvalidPizzaType
from domain.pizza.cheese_pizza import CheesePizza
from domain.pizza.pepperoni_pizza import PepperoniPizza
from domain.pizza.sausage_pizza import SausagePizza
from domain.pizza_id.pizza_id import PizzaId


class InputDTO:
    def __init__(self, pizza_type: str):
        self.pizza_type = pizza_type


class InputDTOFactory:
    @staticmethod
    def build(request_body) -> InputDTO:
        try:
            pizza_type = request_body["pizza_type"]
        except KeyError:
            raise InvalidPizzaType()
        return InputDTO(pizza_type)


class PizzaType:
    CHEESE: int = 1
    PEPPERONI: int = 2
    SAUSAGE: int = 3


class UseCase:
    def __init__(self, pizza_repo: AbstractPizzaRepo, pizza_id_generator: AbstractPizzaIdGenerator,
                 clock: AbstractClock) -> None:
        self.pizza_repo = pizza_repo
        self.pizza_id_generator = pizza_id_generator
        self.clock = clock

    def execute(self, input_dto: InputDTO) -> PizzaId:
        new_id = self.pizza_id_generator.create_new_id()
        current_time = self.clock.current_unix_time_sec()
        if input_dto.pizza_type == "cheese":
            new_pizza = CheesePizza(new_id)
        elif input_dto.pizza_type == "pepperoni":
            new_pizza = PepperoniPizza(new_id)
        elif input_dto.pizza_type == "sausage":
            new_pizza = SausagePizza(new_id)
        else:
            raise InvalidPizzaType()
        new_pizza.start_cooking_at(current_time)
        self.pizza_repo.save(new_pizza)
        return new_id


