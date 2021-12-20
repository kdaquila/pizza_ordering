import pytest

from application.clock import LocalClock
from application.pizza_id_generator import IntegerPizzaIdGenerator
from application.pizza_repo import InMemoryPizzaRepo
from application.use_cases import order_pizza
from domain.exceptions import InvalidPizzaType


@pytest.mark.parametrize("pizza_type, expected_name", [
    ("cheese", "Cheese Pizza"),
    ("pepperoni", "Pepperoni Pizza"),
    ("sausage", "Sausage Pizza")])
def test_order_pizza(pizza_type, expected_name):
    # Arrange
    pizza_repo = InMemoryPizzaRepo()
    input_dto = order_pizza.InputDTOFactory.build({"pizza_type": pizza_type})
    use_case = order_pizza.UseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())

    # Action
    output_dto = use_case.execute(input_dto)

    # Assert
    pizza = pizza_repo.get(output_dto.data.get("pizza_id"))
    assert pizza.name == expected_name


def test_order_invalid_pizza_with_invalid_dto():
    # Arrange / Action / Assert
    with pytest.raises(InvalidPizzaType):
        order_pizza.InputDTOFactory.build({"fake": "fake"})


def test_order_invalid_pizza_with_invalid_pizza_type():
    # Arrange
    order_pizza_use_case = order_pizza.UseCase(InMemoryPizzaRepo(), IntegerPizzaIdGenerator(), LocalClock())

    # Action / Assert
    with pytest.raises(InvalidPizzaType):
        input_dto = order_pizza.InputDTOFactory.build({"pizza_type": "fake"})
        order_pizza_use_case.execute(input_dto)
