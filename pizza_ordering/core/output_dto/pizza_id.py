import uuid


class PizzaId:
    def __init__(self, pizza_id: uuid.UUID):
        self.pizza_id: str = str(pizza_id)