import pytest

from application.pizza_use_cases.order_pizza_use_case import OrderPizzaUseCase, PizzaType
from domain.exceptions import InvalidPizzaType
from unittests.in_memory_pizza_repo import InMemoryPizzaRepo
from unittests.integer_order_id_maker import IntegerPizzaIdGenerator
from application.clock.local_clock import LocalClock


def test_create_cheese_pizza_order():
    # Arrange
    clock = LocalClock()
    order_id_maker = IntegerPizzaIdGenerator()
    pizza_repo = InMemoryPizzaRepo()
    use_case = OrderPizzaUseCase(pizza_repo, order_id_maker, clock)

    # Action
    order_id = use_case.execute(PizzaType.CHEESE)

    # Assert
    pizza = pizza_repo.get(order_id)
    assert pizza.name == "Cheese Pizza"


def test_create_pepperoni_pizza_order():
    # Arrange
    clock = LocalClock()
    order_id_maker = IntegerPizzaIdGenerator()
    pizza_repo = InMemoryPizzaRepo()
    use_case = OrderPizzaUseCase(pizza_repo, order_id_maker, clock)

    # Action
    order_id = use_case.execute(PizzaType.PEPPERONI)

    # Assert
    pizza = pizza_repo.get(order_id)
    assert pizza.name == "Pepperoni Pizza"


def test_create_sausage_pizza_order():
    # Arrange
    clock = LocalClock()
    order_id_maker = IntegerPizzaIdGenerator()
    pizza_repo = InMemoryPizzaRepo()
    use_case = OrderPizzaUseCase(pizza_repo, order_id_maker, clock)

    # Action
    order_id = use_case.execute(PizzaType.SAUSAGE)

    # Assert
    pizza = pizza_repo.get(order_id)
    assert pizza.name == "Sausage Pizza"


def test_create_invalid_pizza_type():
    # Arrange
    clock = LocalClock()
    order_id_maker = IntegerPizzaIdGenerator()
    pizza_repo = InMemoryPizzaRepo()
    use_case = OrderPizzaUseCase(pizza_repo, order_id_maker, clock)

    # Action / Assert
    with pytest.raises(InvalidPizzaType):
        pizza_type = -5
        order_id = use_case.execute(pizza_type)