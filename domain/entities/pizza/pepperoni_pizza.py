from domain.entities.pizza.base_pizza import BasePizza


class PepperoniPizza(BasePizza):
    def __init__(self, pizza_id, ):
        super().__init__(pizza_id, "Pepperoni Pizza", "Pizza crust with mozarella cheese and pepperoni over tomato sauce")
