from injector import Injector

from core.use_cases.find_pizza import FindPizzaUseCase
from unittests.container import Container
from core.use_cases.order_pizza import OrderPizzaInputDTOFactory, OrderPizzaUseCase


def test_find_all_pizzas():
    # Arrange
    use_case_injector = Injector([Container])
    input_dto = OrderPizzaInputDTOFactory.build({"pizza_type": "cheese"})
    order_pizza_use_case = use_case_injector.get(OrderPizzaUseCase)
    order_pizza_use_case.execute(input_dto)
    order_pizza_use_case.execute(input_dto)
    order_pizza_use_case.execute(input_dto)
    find_pizza_use_case = use_case_injector.get(FindPizzaUseCase)

    # Action
    output_dto = find_pizza_use_case.execute()

    # Assert
    assert len(output_dto.data.get("pizzas")) == 3
