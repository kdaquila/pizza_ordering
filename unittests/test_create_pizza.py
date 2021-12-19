import pytest

from application.clock.local_clock import LocalClock
from application.pizza_use_cases.order_pizza_use_case import OrderPizzaUseCase, PizzaType
from domain.exceptions import InvalidPizzaType
from unittests.mocks.in_memory_pizza_repo import InMemoryPizzaRepo
from unittests.mocks.integer_pizza_id_generator import IntegerPizzaIdGenerator


@pytest.mark.parametrize("pizza_type, expected_name", [
    (PizzaType.CHEESE, "Cheese Pizza"),
    (PizzaType.PEPPERONI, "Pepperoni Pizza"),
    (PizzaType.SAUSAGE, "Sausage Pizza")])
def test_create_pizza(pizza_type, expected_name):
    # Arrange
    pizza_repo = InMemoryPizzaRepo()
    use_case = OrderPizzaUseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())

    # Action
    order_id = use_case.execute(pizza_type)

    # Assert
    pizza = pizza_repo.get(order_id)
    assert pizza.name == expected_name


def test_create_invalid_pizza_type():
    # Arrange
    use_case = OrderPizzaUseCase(InMemoryPizzaRepo(), IntegerPizzaIdGenerator(), LocalClock())

    # Action / Assert
    with pytest.raises(InvalidPizzaType):
        pizza_type = -5
        use_case.execute(pizza_type)
