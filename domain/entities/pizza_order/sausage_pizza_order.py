from domain.entities.pizza_order.base_pizza_order import BasePizzaOrder


class SausagePizzaOrder(BasePizzaOrder):
    def __init__(self, order_id, ):
        super().__init__(order_id, "Sausage Pizza", "Pizza crust with mozarella cheese and sausage over tomato sauce")
