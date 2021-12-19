from application.clock.clock import Clock
from application.order_id.order_id_maker import OrderIdMaker
from application.order_repo.pizza_order_repo import PizzaOrderRepo
from domain.entities.pizza_order.cheese_pizza_order import CheesePizzaOrder
from domain.entities.pizza_order.pepperoni_pizza_order import PepperoniPizzaOrder
from domain.entities.pizza_order.sausage_pizza_order import SausagePizzaOrder
from domain.exceptions import InvalidPizzaType
from domain.value_objects import OrderId


class PizzaType:
    CHEESE: int = 1
    PEPPERONI: int = 2
    SAUSAGE: int = 3


class OrderPizza:
    def __init__(self, pizza_repo: PizzaOrderRepo, order_id_maker: OrderIdMaker, clock: Clock) -> None:
        self.pizza_repo = pizza_repo
        self.order_id_maker = order_id_maker
        self.clock = clock

    def execute(self, pizza_type: int) -> OrderId:
        new_id = self.order_id_maker.create_new_id()
        current_time = self.clock.current_unix_time_sec()
        if pizza_type == PizzaType.CHEESE:
            new_pizza = CheesePizzaOrder(new_id)
        elif pizza_type == PizzaType.PEPPERONI:
            new_pizza = PepperoniPizzaOrder(new_id)
        elif pizza_type == PizzaType.SAUSAGE:
            new_pizza = SausagePizzaOrder(new_id)
        else:
            raise InvalidPizzaType()
        new_pizza.start_cooking_at(current_time)
        self.pizza_repo.save(new_pizza)
        return new_id
