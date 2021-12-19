import pytest

from application.order_use_cases.cancel_pizza import CancelPizza
from domain.entities.pizza_order.cheese_pizza_order import CheesePizzaOrder
from domain.entities.pizza_order.pepperoni_pizza_order import PepperoniPizzaOrder
from domain.entities.pizza_order.sausage_pizza_order import SausagePizzaOrder
from application.order_use_cases.order_pizza import OrderPizza, PizzaType
from domain.exceptions import InvalidPizzaType, CannotCancelOrder
from unittests.in_memory_pizza_repo import InMemoryPizzaRepo
from unittests.integer_order_id_maker import IntegerOrderIdMaker
from unittests.local_clock import LocalClock
import config


def test_cancel_cheese_pizza_order():
    # Arrange
    clock = LocalClock()
    order_id_maker = IntegerOrderIdMaker()
    pizza_repo = InMemoryPizzaRepo()
    create_pizza_use_case = OrderPizza(pizza_repo, order_id_maker, clock)
    order_id = create_pizza_use_case.execute(PizzaType.CHEESE)
    cancel_pizza_use_case = CancelPizza(pizza_repo, clock)

    # Action
    cancel_pizza_use_case.execute(order_id)

    # Assert
    pizza = pizza_repo.get(order_id)
    assert pizza.is_cooking is False


def test_fail_to_cancel_cheese_pizza_order():
    # Arrange
    time_shift_sec = config.cancel_order_interval_sec + 15
    order_id_maker = IntegerOrderIdMaker()
    pizza_repo = InMemoryPizzaRepo()
    create_pizza_use_case = OrderPizza(pizza_repo, order_id_maker, LocalClock())
    order_id = create_pizza_use_case.execute(PizzaType.CHEESE)
    cancel_pizza_use_case = CancelPizza(pizza_repo, LocalClock(time_shift_sec))

    # Action / Assert
    with pytest.raises(CannotCancelOrder):
        cancel_pizza_use_case.execute(order_id)
