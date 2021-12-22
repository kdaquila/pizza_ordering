import pytest
from injector import Injector

from core.exceptions import InvalidPizzaType
from unittests.container import Container
from core.use_cases.order_pizza import OrderPizzaInputDTOFactory, OrderPizzaUseCase


@pytest.mark.parametrize("pizza_type, expected_name", [
    ("cheese", "Cheese Pizza"),
    ("pepperoni", "Pepperoni Pizza"),
    ("sausage", "Sausage Pizza")])
def test_order_pizza(pizza_type, expected_name):
    # Arrange
    input_dto = OrderPizzaInputDTOFactory.build({"pizza_type": pizza_type})
    use_case_injector = Injector([Container])
    order_pizza_use_case = use_case_injector.get(OrderPizzaUseCase)

    # Action
    output_dto = order_pizza_use_case.execute(input_dto)

    # Assert
    assert output_dto.data["pizza_id"] == 1


def test_order_invalid_pizza_with_invalid_dto():
    # Arrange / Action / Assert
    with pytest.raises(InvalidPizzaType):
        OrderPizzaInputDTOFactory.build({"fake": "fake"})


def test_order_invalid_pizza_with_invalid_pizza_type():
    # Arrange
    use_case_injector = Injector([Container])
    order_pizza_use_case = use_case_injector.get(OrderPizzaUseCase)

    # Action / Assert
    with pytest.raises(InvalidPizzaType):
        input_dto = OrderPizzaInputDTOFactory.build({"pizza_type": "fake"})
        order_pizza_use_case.execute(input_dto)
