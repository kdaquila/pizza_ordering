from src.application.pizza_use_cases.order_pizza.order_pizza_input_dto import OrderPizzaInputDTO
from src.application.pizza_use_cases.order_pizza.order_pizza_use_case import OrderPizzaUseCase
from src.domain.exceptions import InvalidPizzaType


class OrderPizzaInputDTOService:
    @staticmethod
    def build_dto(request_body) -> OrderPizzaInputDTO:
        pizza_type = request_body.get("pizza_type", None)
        pizza_type_id = None
        if pizza_type == "cheese":
            pizza_type_id = OrderPizzaUseCase.PizzaType.CHEESE
        elif pizza_type == "pepperoni":
            pizza_type_id = OrderPizzaUseCase.PizzaType.PEPPERONI
        elif pizza_type == "sausage":
            pizza_type_id = OrderPizzaUseCase.PizzaType.SAUSAGE
        else:
            raise InvalidPizzaType()
        return OrderPizzaInputDTO(pizza_type_id)
