from src.domain.entities.pizza.base_pizza import BasePizza


class GetPizzasOutputDTO:
    def __init__(self, pizzas: [BasePizza]):
        self.pizzas: [BasePizza] = pizzas
