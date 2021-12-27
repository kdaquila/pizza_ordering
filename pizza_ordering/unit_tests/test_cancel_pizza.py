import uuid

import pytest

from pizza_ordering.core.exceptions import CannotCancelPizza, PizzaNotFound, PizzaNotCooking
from pizza_ordering.core.use_cases.cancel_pizza import CancelPizzaUseCase
from pizza_ordering.core.use_cases.order_pizza import OrderPizzaUseCase
from pizza_ordering.core.pizza_repo import AbstractPizzaRepo
from .clock import FastClock
from .container import container


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "veggie"])
def test_cancel_pizza(pizza_type):
    # Arrange
    order_pizza_use_case = container.get(OrderPizzaUseCase)
    order_pizza_output_dto = order_pizza_use_case.execute(pizza_type)
    pizza_id = order_pizza_output_dto.pizza_id
    cancel_pizza_use_case = container.get(CancelPizzaUseCase)

    # Action
    cancel_pizza_use_case.execute(uuid.UUID(pizza_id))

    # Assert
    pass


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "veggie"])
def test_cancel_pizza_twice(pizza_type):
    # Arrange
    order_pizza_use_case = container.get(OrderPizzaUseCase)
    order_pizza_output_dto = order_pizza_use_case.execute(pizza_type)
    pizza_id = order_pizza_output_dto.pizza_id
    cancel_pizza_use_case = container.get(CancelPizzaUseCase)

    # Action / Assert
    cancel_pizza_use_case.execute(uuid.UUID(pizza_id))
    with pytest.raises(PizzaNotCooking):
        cancel_pizza_use_case.execute(uuid.UUID(pizza_id))


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "veggie"])
def test_fail_to_cancel_pizza_because_too_late(pizza_type):
    # Arrange
    order_pizza_use_case = container.get(OrderPizzaUseCase)
    order_pizza_output_dto = order_pizza_use_case.execute(pizza_type)
    pizza_id = order_pizza_output_dto.pizza_id
    pizza_repo = container.get(AbstractPizzaRepo)
    cancel_pizza_use_case = CancelPizzaUseCase(pizza_repo, FastClock())

    # Action / Assert
    with pytest.raises(CannotCancelPizza):
        cancel_pizza_use_case.execute(uuid.UUID(pizza_id))


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "veggie"])
def test_fail_to_cancel_pizza_because_pizza_not_found(pizza_type):
    # Arrange
    fake_pizza_id = -5
    cancel_pizza_use_case = container.get(CancelPizzaUseCase)

    # Action / Assert
    with pytest.raises(PizzaNotFound):
        cancel_pizza_use_case.execute(fake_pizza_id)

