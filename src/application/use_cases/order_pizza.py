from application.clock import AbstractClock
from application.pizza_id_generator import AbstractPizzaIdGenerator
from application.pizza_repo import AbstractPizzaRepo
from domain.exceptions import InvalidPizzaType
from domain.pizza import CheesePizza
from domain.pizza import PepperoniPizza
from domain.pizza import SausagePizza
from domain.pizza_id import PizzaId


class InputDTO:
    def __init__(self, pizza_type: str):
        self.pizza_type = pizza_type


class OutputDTO:
    def __init__(self, status: str, message: str, pizza_id: PizzaId):
        self.status = status
        self.message = message
        self.data = {"pizza_id": pizza_id}


class InputDTOFactory:
    @staticmethod
    def build(request_body) -> InputDTO:
        pizza_type = request_body.get("pizza_type")
        if pizza_type is None or pizza_type not in ["cheese", "pepperoni", "sausage"]:
            raise InvalidPizzaType()
        return InputDTO(pizza_type)


class UseCase:
    def __init__(self, pizza_repo: AbstractPizzaRepo, pizza_id_generator: AbstractPizzaIdGenerator,
                 clock: AbstractClock) -> None:
        self.pizza_repo = pizza_repo
        self.pizza_id_generator = pizza_id_generator
        self.clock = clock

    def execute(self, input_dto: InputDTO) -> OutputDTO:
        new_id = self.pizza_id_generator.create_new_id()
        current_time = self.clock.current_unix_time_sec()
        pizza_mapping = {"cheese": CheesePizza, "pepperoni": PepperoniPizza, "sausage": SausagePizza}
        new_pizza_type = pizza_mapping[input_dto.pizza_type]
        new_pizza = new_pizza_type(new_id)
        new_pizza.start_cooking_at(current_time)
        self.pizza_repo.save(new_pizza)
        return OutputDTO("success", "", new_id)
