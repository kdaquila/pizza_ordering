from domain.entities.pizza.base_pizza import BasePizza


class SausagePizza(BasePizza):
    def __init__(self, pizza_id, ):
        super().__init__(pizza_id, "Sausage Pizza", "Pizza crust with mozarella cheese and sausage over tomato sauce")
