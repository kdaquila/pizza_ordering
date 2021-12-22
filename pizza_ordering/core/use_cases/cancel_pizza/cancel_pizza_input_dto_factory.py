from . import CancelPizzaInputDTO
from pizza_ordering.core.exceptions import InvalidPizzaId


class CancelPizzaInputDTOFactory:
    @staticmethod
    def build(pizza_id) -> CancelPizzaInputDTO:
        CancelPizzaInputDTOFactory.validate_integer(pizza_id)
        return CancelPizzaInputDTO(pizza_id)

    @staticmethod
    def validate_integer(value) -> None:
        try:
            int(value)
        except TypeError:
            raise InvalidPizzaId
