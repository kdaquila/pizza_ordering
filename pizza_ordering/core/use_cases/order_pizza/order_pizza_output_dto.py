from pizza_ordering.core.pizza_id import PizzaId


class OrderPizzaOutputDTO:
    def __init__(self, pizza_id: PizzaId):
        self.pizza_id = pizza_id