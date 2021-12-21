import pytest
from injector import Injector

from application.cancel_pizza import CancelPizzaUseCase, CancelPizzaInputDTOFactory
from application.pizza_repo import AbstractPizzaRepo
from domain.exceptions import CannotCancelPizza, PizzaNotFound
from unittests.clock.fast_clock import FastClock
from unittests.container import Container
from application.order_pizza import OrderPizzaUseCase, OrderPizzaInputDTOFactory


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "sausage"])
def test_cancel_pizza(pizza_type):
    # Arrange
    use_case_injector = Injector([Container])

    order_pizza_use_case = use_case_injector.get(OrderPizzaUseCase)
    order_pizza_input_dto = OrderPizzaInputDTOFactory.build({"pizza_type": pizza_type})
    order_pizza_output_dto = order_pizza_use_case.execute(order_pizza_input_dto)

    cancel_pizza_input_dto = CancelPizzaInputDTOFactory.build(order_pizza_output_dto.data["pizza_id"])
    cancel_pizza_use_case = use_case_injector.get(CancelPizzaUseCase)

    # Action
    cancel_pizza_output_dto = cancel_pizza_use_case.execute(cancel_pizza_input_dto)

    # Assert
    assert cancel_pizza_output_dto.status == "success"


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "sausage"])
def test_cancel_pizza_twice(pizza_type):
    # Arrange
    use_case_injector = Injector([Container])

    order_pizza_use_case = use_case_injector.get(OrderPizzaUseCase)
    order_pizza_input_dto = OrderPizzaInputDTOFactory.build({"pizza_type": pizza_type})
    order_pizza_output_dto = order_pizza_use_case.execute(order_pizza_input_dto)

    cancel_pizza_input_dto = CancelPizzaInputDTOFactory.build(order_pizza_output_dto.data["pizza_id"])
    cancel_pizza_use_case = use_case_injector.get(CancelPizzaUseCase)

    # Action
    cancel_pizza_use_case.execute(cancel_pizza_input_dto)
    cancel_pizza_output_dto = cancel_pizza_use_case.execute(cancel_pizza_input_dto)

    # Assert
    assert cancel_pizza_output_dto.status == "fail"


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "sausage"])
def test_fail_to_cancel_pizza_because_too_late(pizza_type):
    # Arrange
    use_case_injector = Injector([Container])

    order_pizza_use_case = use_case_injector.get(OrderPizzaUseCase)
    order_pizza_input_dto = OrderPizzaInputDTOFactory.build({"pizza_type": pizza_type})
    order_pizza_output_dto = order_pizza_use_case.execute(order_pizza_input_dto)
    pizza_id = order_pizza_output_dto.data["pizza_id"]

    cancel_pizza_input_dto = CancelPizzaInputDTOFactory.build(pizza_id)
    pizza_repo = use_case_injector.get(AbstractPizzaRepo)
    cancel_pizza_use_case = CancelPizzaUseCase(pizza_repo, FastClock())

    # Action
    cancel_pizza_output_dto = cancel_pizza_use_case.execute(cancel_pizza_input_dto)

    # Assert
    assert cancel_pizza_output_dto.status == "fail"


@pytest.mark.parametrize("pizza_type", ["cheese", "pepperoni", "sausage"])
def test_fail_to_cancel_pizza_because_pizza_not_found(pizza_type):
    # Arrange
    use_case_injector = Injector([Container])
    fake_pizza_id = -5
    cancel_pizza_input_dto = CancelPizzaInputDTOFactory.build(fake_pizza_id)
    cancel_pizza_use_case = use_case_injector.get(CancelPizzaUseCase)

    # Action
    cancel_pizza_output_dto = cancel_pizza_use_case.execute(cancel_pizza_input_dto)

    # Assert
    assert cancel_pizza_output_dto.status == "fail"

