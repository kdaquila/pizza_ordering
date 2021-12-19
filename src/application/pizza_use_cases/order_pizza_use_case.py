from src.application.clock.abstract_clock import AbstractClock
from src.application.pizza_id.abstract_pizza_id_generator import AbstractPizzaIdGenerator
from src.application.pizza_repo.abstract_pizza_repo import AbstractPizzaRepo
from src.domain.entities.pizza.cheese_pizza import CheesePizza
from src.domain.entities.pizza.pepperoni_pizza import PepperoniPizza
from src.domain.entities.pizza.sausage_pizza import SausagePizza
from src.domain.exceptions import InvalidPizzaType
from src.domain.value_objects.pizza_id import PizzaId


class PizzaType:
    CHEESE: int = 1
    PEPPERONI: int = 2
    SAUSAGE: int = 3


class OrderPizzaUseCase:
    def __init__(self, pizza_repo: AbstractPizzaRepo, order_id_maker: AbstractPizzaIdGenerator, clock: AbstractClock) -> None:
        self.pizza_repo = pizza_repo
        self.pizza_id_generator = order_id_maker
        self.clock = clock

    def execute(self, pizza_type: int) -> PizzaId:
        new_id = self.pizza_id_generator.create_new_id()
        current_time = self.clock.current_unix_time_sec()
        if pizza_type == PizzaType.CHEESE:
            new_pizza = CheesePizza(new_id)
        elif pizza_type == PizzaType.PEPPERONI:
            new_pizza = PepperoniPizza(new_id)
        elif pizza_type == PizzaType.SAUSAGE:
            new_pizza = SausagePizza(new_id)
        else:
            raise InvalidPizzaType()
        new_pizza.start_cooking_at(current_time)
        self.pizza_repo.save(new_pizza)
        return new_id
