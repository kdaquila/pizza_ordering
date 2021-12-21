import abc

from domain.pizza import BasePizza


class AbstractPizzaFactory:
    @abc.abstractmethod
    def build(self, pizza_type: str) -> BasePizza:
        pass
