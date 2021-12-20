from src.domain.value_objects.pizza_id import PizzaId


class CancelPizzaInputDTO:
    def __init__(self, pizza_id: PizzaId) -> None:
        self.pizza_id = pizza_id
