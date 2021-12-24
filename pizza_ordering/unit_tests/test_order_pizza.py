import uuid

import pytest
from injector import Injector

from pizza_ordering.core.exceptions import InvalidPizzaType
from pizza_ordering.core.use_cases.order_pizza import OrderPizzaUseCase
from .container import Container


@pytest.mark.parametrize("pizza_type, expected_name", [
    ("cheese", "Cheese Pizza"),
    ("pepperoni", "Pepperoni Pizza"),
    ("sausage", "Sausage Pizza")])
def test_order_pizza(pizza_type, expected_name):
    # Arrange
    use_case_injector = Injector([Container])
    order_pizza_use_case = use_case_injector.get(OrderPizzaUseCase)

    # Action
    output_dto = order_pizza_use_case.execute(pizza_type)

    # Assert
    uuid.UUID(output_dto.pizza_id)


def test_order_invalid_pizza_with_invalid_pizza_type():
    # Arrange
    use_case_injector = Injector([Container])
    order_pizza_use_case = use_case_injector.get(OrderPizzaUseCase)

    # Action / Assert
    with pytest.raises(InvalidPizzaType):
        order_pizza_use_case.execute(pizza_type="fake")
