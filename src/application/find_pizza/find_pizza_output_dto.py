from domain.pizza import BasePizza


class FindPizzaOutputDTO:
    def __init__(self, pizzas: [BasePizza], status: str = "", message: str = ""):
        self.status = status
        self.message = message
        self.data = {"pizzas": pizzas}