from injector import Injector

from application.find_pizza.find_pizza_use_case import FindPizzaUseCase
from unittests.container import Container
from application.order_pizza import OrderPizzaInputDTOFactory, OrderPizzaUseCase


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
