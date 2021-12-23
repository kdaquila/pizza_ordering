from injector import Injector

from pizza_ordering.core.use_cases.find_pizza import FindPizzaUseCase
from pizza_ordering.core.use_cases.order_pizza import OrderPizzaInputDTOFactory, OrderPizzaUseCase
from .container import Container


def test_find_all_pizzas():
    # Arrange
    use_case_injector = Injector([Container])
    pizza_type = "cheese"
    order_pizza_use_case = use_case_injector.get(OrderPizzaUseCase)
    order_pizza_use_case.execute(pizza_type)
    order_pizza_use_case.execute(pizza_type)
    order_pizza_use_case.execute(pizza_type)
    find_pizza_use_case = use_case_injector.get(FindPizzaUseCase)

    # Action
    output_dto = find_pizza_use_case.execute()

    # Assert
    assert len(output_dto.data.get("pizzas")) == 3
