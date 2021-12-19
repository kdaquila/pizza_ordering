from domain.entities.pizza_order.base_pizza_order import BasePizzaOrder


class CheesePizzaOrder(BasePizzaOrder):
    def __init__(self, order_id, ):
        super().__init__(order_id, "Cheese Pizza", "Pizza crust with only Mozarella cheese over tomato sauce")
