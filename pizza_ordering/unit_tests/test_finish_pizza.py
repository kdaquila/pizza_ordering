from uuid import UUID

import pytest

from pizza_ordering.core.exceptions import PizzaNotCooking, PizzaNotFound
from pizza_ordering.core.use_cases.order_pizza import OrderPizzaUseCase
from pizza_ordering.core.use_cases.finish_pizza import FinishPizzaUseCase
from .container import container


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "veggie"])
def test_finish_pizza(pizza_type):
    # Arrange
    order_pizza_use_case = container.get(OrderPizzaUseCase)
    order_pizza_output_dto = order_pizza_use_case.execute(pizza_type)
    pizza_id = order_pizza_output_dto.pizza_id
    finish_pizza_use_case = container.get(FinishPizzaUseCase)

    # Action
    finish_pizza_use_case.execute(UUID(pizza_id))

    # Assert
    pass


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "veggie"])
def test_finish_pizza_twice(pizza_type):
    # Arrange
    order_pizza_use_case = container.get(OrderPizzaUseCase)
    order_pizza_output_dto = order_pizza_use_case.execute(pizza_type)
    pizza_id = order_pizza_output_dto.pizza_id
    finish_pizza_use_case = container.get(FinishPizzaUseCase)

    # Action / Assert
    finish_pizza_use_case.execute(UUID(pizza_id))
    with pytest.raises(PizzaNotCooking):
        finish_pizza_use_case.execute(UUID(pizza_id))


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "veggie"])
def test_fail_to_finish_pizza_because_pizza_not_found(pizza_type):
    # Arrange
    fake_pizza_id = -5
    finish_pizza_use_case = container.get(FinishPizzaUseCase)

    # Action / Assert
    with pytest.raises(PizzaNotFound):
        finish_pizza_use_case.execute(fake_pizza_id)
