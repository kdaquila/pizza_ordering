import abc

from pizza_ordering.core.entities.pizza import BasePizza


class AbstractPizzaFactory:
    @abc.abstractmethod
    def build(self, pizza_type: str) -> BasePizza:
        pass
