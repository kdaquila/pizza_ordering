from . import BasePizza


class CheesePizza(BasePizza):
    def __init__(self, pizza_id, ):
        super().__init__(pizza_id, "Cheese Pizza", "Pizza crust with only Mozarella cheese over tomato sauce")
