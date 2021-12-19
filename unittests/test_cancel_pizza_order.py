import pytest

from application.pizza_use_cases.cancel_pizza import CancelPizzaUseCase
from application.pizza_use_cases.order_pizza_use_case import OrderPizzaUseCase, PizzaType
from domain.exceptions import CannotCancelPizza
from unittests.in_memory_pizza_repo import InMemoryPizzaRepo
from unittests.integer_order_id_maker import IntegerPizzaIdGenerator
from application.clock.local_clock import LocalClock
import config


def test_cancel_cheese_pizza_order():
    # Arrange
    clock = LocalClock()
    order_id_maker = IntegerPizzaIdGenerator()
    pizza_repo = InMemoryPizzaRepo()
    create_pizza_use_case = OrderPizzaUseCase(pizza_repo, order_id_maker, clock)
    order_id = create_pizza_use_case.execute(PizzaType.CHEESE)
    cancel_pizza_use_case = CancelPizzaUseCase(pizza_repo, clock)

    # Action
    cancel_pizza_use_case.execute(order_id)

    # Assert
    pizza = pizza_repo.get(order_id)
    assert pizza.is_cooking is False


def test_fail_to_cancel_cheese_pizza_order():
    # Arrange
    time_shift_sec = config.cancel_order_interval_sec + 15
    order_id_maker = IntegerPizzaIdGenerator()
    pizza_repo = InMemoryPizzaRepo()
    create_pizza_use_case = OrderPizzaUseCase(pizza_repo, order_id_maker, LocalClock())
    order_id = create_pizza_use_case.execute(PizzaType.CHEESE)
    cancel_pizza_use_case = CancelPizzaUseCase(pizza_repo, LocalClock(time_shift_sec))

    # Action / Assert
    with pytest.raises(CannotCancelPizza):
        cancel_pizza_use_case.execute(order_id)
