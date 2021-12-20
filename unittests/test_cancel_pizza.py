import pytest

import config
from application.clock import LocalClock
from application.pizza_id_generator import IntegerPizzaIdGenerator
from application.pizza_repo import InMemoryPizzaRepo
from application.use_cases import cancel_pizza, order_pizza
from domain.exceptions import CannotCancelPizza, PizzaNotFound


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "sausage"])
def test_cancel_pizza(pizza_type):
    # Arrange
    pizza_repo = InMemoryPizzaRepo()
    order_pizza_use_case = order_pizza.UseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())
    pizza_id = order_pizza_use_case.execute(order_pizza.InputDTO(pizza_type))
    cancel_pizza_use_case = cancel_pizza.UseCase(pizza_repo, LocalClock())

    # Action
    cancel_pizza_use_case.execute(cancel_pizza.InputDTO(pizza_id))

    # Assert
    pizza = pizza_repo.get(pizza_id)
    assert pizza.is_cooking is False


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "sausage"])
def test_fail_to_cancel_pizza_because_too_late(pizza_type):
    # Arrange
    time_shift_sec = config.cancel_order_interval_sec + 15
    pizza_repo = InMemoryPizzaRepo()
    order_pizza_use_case = order_pizza.UseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())
    input_dto = order_pizza.InputDTO(pizza_type)
    pizza_id = order_pizza_use_case.execute(input_dto)
    cancel_pizza_use_case = cancel_pizza.UseCase(pizza_repo, LocalClock(time_shift_sec))

    # Action / Assert
    with pytest.raises(CannotCancelPizza):
        cancel_pizza_use_case.execute(cancel_pizza.InputDTO(pizza_id))


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "sausage"])
def test_fail_to_cancel_pizza_because_pizza_not_found(pizza_type):
    # Arrange
    cancel_pizza_use_case = cancel_pizza.UseCase(InMemoryPizzaRepo(), LocalClock())

    # Action / Assert
    with pytest.raises(PizzaNotFound):
        fake_pizza_id = -5
        cancel_pizza_use_case.execute(cancel_pizza.InputDTO(fake_pizza_id))
