from domain.entities.pizza_order.base_pizza_order import BasePizzaOrder


class PepperoniPizzaOrder(BasePizzaOrder):
    def __init__(self, order_id, ):
        super().__init__(order_id, "Pepperoni Pizza", "Pizza crust with mozarella cheese and pepperoni over tomato sauce")
