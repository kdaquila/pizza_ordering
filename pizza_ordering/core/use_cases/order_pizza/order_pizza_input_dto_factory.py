from . import OrderPizzaInputDTO
from pizza_ordering.core.exceptions import InvalidPizzaType


class OrderPizzaInputDTOFactory:
    @staticmethod
    def build(request_body: dict) -> OrderPizzaInputDTO:
        pizza_type = request_body.get("pizza_type")
        if pizza_type is None or pizza_type not in ["cheese", "pepperoni", "sausage"]:
            raise InvalidPizzaType()
        return OrderPizzaInputDTO(pizza_type)