import pytest

from src.application.clock.local_clock import LocalClock
from application.pizza_use_cases.order_pizza.order_pizza_use_case import OrderPizzaUseCase
from application.pizza_use_cases.order_pizza.order_pizza_input_dto import OrderPizzaInputDTO
from src.domain.exceptions import InvalidPizzaType
from application.pizza_repo.in_memory_pizza_repo import InMemoryPizzaRepo
from application.pizza_id_generator.integer_pizza_id_generator import IntegerPizzaIdGenerator


@pytest.mark.parametrize("pizza_type, expected_name", [
    (OrderPizzaUseCase.PizzaType.CHEESE, "Cheese Pizza"),
    (OrderPizzaUseCase.PizzaType.PEPPERONI, "Pepperoni Pizza"),
    (OrderPizzaUseCase.PizzaType.SAUSAGE, "Sausage Pizza")])
def test_create_pizza(pizza_type, expected_name):
    # Arrange
    pizza_repo = InMemoryPizzaRepo()
    input_dto = OrderPizzaInputDTO(pizza_type)
    use_case = OrderPizzaUseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())

    # Action
    order_id = use_case.execute(input_dto)

    # Assert
    pizza = pizza_repo.get(order_id)
    assert pizza.name == expected_name


def test_create_invalid_pizza_type():
    # Arrange
    order_pizza_use_case = OrderPizzaUseCase(InMemoryPizzaRepo(), IntegerPizzaIdGenerator(), LocalClock())

    # Action / Assert
    with pytest.raises(InvalidPizzaType):
        pizza_type = -5
        input_dto = OrderPizzaInputDTO(pizza_type)
        order_pizza_use_case.execute(input_dto)
