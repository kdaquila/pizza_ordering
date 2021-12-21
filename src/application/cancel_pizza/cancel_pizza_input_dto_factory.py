from application.cancel_pizza.cancel_pizza_input_dto import CancelPizzaInputDTO


class CancelPizzaInputDTOFactory:
    @staticmethod
    def build(pizza_id) -> CancelPizzaInputDTO:
        CancelPizzaInputDTOFactory.validate_integer(pizza_id)
        return CancelPizzaInputDTO(pizza_id)

    @staticmethod
    def validate_integer(value) -> None:
        int(value)