from application.clock.local_clock import LocalClock
from application.pizza_use_cases.get_pizza_use_case import GetPizzaUseCase
from application.pizza_use_cases.order_pizza_use_case import OrderPizzaUseCase, PizzaType
from unittests.mocks.in_memory_pizza_repo import InMemoryPizzaRepo
from unittests.mocks.integer_pizza_id_generator import IntegerPizzaIdGenerator


def test_get_all_pizzas():
    # Arrange
    pizza_repo = InMemoryPizzaRepo()
    order_pizza_use_case = OrderPizzaUseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())
    order_pizza_use_case.execute(PizzaType.CHEESE)
    order_pizza_use_case.execute(PizzaType.CHEESE)
    order_pizza_use_case.execute(PizzaType.CHEESE)
    get_pizza_use_case = GetPizzaUseCase(pizza_repo, LocalClock())

    # Action
    pizzas = get_pizza_use_case.execute()

    # Assert
    assert len(pizzas) == 3
