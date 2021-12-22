from pizza_ordering.core.pizza_id import PizzaId


class OrderPizzaOutputDTO:
    def __init__(self, status: str, message: str, pizza_id: PizzaId):
        self.status = status
        self.message = message
        self.data = {"pizza_id": pizza_id}