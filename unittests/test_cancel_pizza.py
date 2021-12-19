import pytest

from application.pizza_use_cases.cancel_pizza import CancelPizzaUseCase
from application.pizza_use_cases.order_pizza_use_case import OrderPizzaUseCase, PizzaType
from domain.exceptions import CannotCancelPizza
from unittests.mocks.in_memory_pizza_repo import InMemoryPizzaRepo
from unittests.mocks.integer_pizza_id_generator import IntegerPizzaIdGenerator
from application.clock.local_clock import LocalClock
import config


@pytest.mark.parametrize("pizza_type", [PizzaType.CHEESE, PizzaType.PEPPERONI, PizzaType.SAUSAGE])
def test_cancel_pizza(pizza_type):
    # Arrange
    pizza_repo = InMemoryPizzaRepo()
    create_pizza_use_case = OrderPizzaUseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())
    pizza_id = create_pizza_use_case.execute(pizza_type)
    cancel_pizza_use_case = CancelPizzaUseCase(pizza_repo, LocalClock())

    # Action
    cancel_pizza_use_case.execute(pizza_id)

    # Assert
    pizza = pizza_repo.get(pizza_id)
    assert pizza.is_cooking is False


@pytest.mark.parametrize("pizza_type", [PizzaType.CHEESE, PizzaType.PEPPERONI, PizzaType.SAUSAGE])
def test_fail_to_cancel_pizza(pizza_type):
    # Arrange
    time_shift_sec = config.cancel_order_interval_sec + 15
    pizza_repo = InMemoryPizzaRepo()
    create_pizza_use_case = OrderPizzaUseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())
    pizza_id = create_pizza_use_case.execute(pizza_type)
    cancel_pizza_use_case = CancelPizzaUseCase(pizza_repo, LocalClock(time_shift_sec))

    # Action / Assert
    with pytest.raises(CannotCancelPizza):
        cancel_pizza_use_case.execute(pizza_id)
