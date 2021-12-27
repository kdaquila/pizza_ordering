import uuid

import pytest
from injector import Injector

from pizza_ordering.core.exceptions import InvalidPizzaType, PizzaNotFound
from pizza_ordering.core.use_cases.order_pizza import OrderPizzaUseCase
from pizza_ordering.core.use_cases.delete_pizza import DeletePizzaUseCase
from .container import Container


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "veggie"])
def test_delete_pizza(pizza_type):
    # Arrange
    use_case_injector = Injector([Container])
    order_pizza_use_case = use_case_injector.get(OrderPizzaUseCase)
    order_pizza_use_case.execute(pizza_type)
    delete_pizza_use_case = use_case_injector.get(DeletePizzaUseCase)

    # Action / Action
    delete_pizza_use_case.execute()


def test_order_invalid_pizza_with_invalid_pizza_type():
    # Arrange
    use_case_injector = Injector([Container])
    delete_pizza_use_case = use_case_injector.get(DeletePizzaUseCase)

    # Action / Assert
    with pytest.raises(PizzaNotFound):
        delete_pizza_use_case.execute()
