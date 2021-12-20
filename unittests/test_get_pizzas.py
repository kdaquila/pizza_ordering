from src.application.clock.local_clock import LocalClock
from application.pizza_use_cases.get_all_pizzas.get_pizzas_use_case import GetPizzaUseCase
from application.pizza_use_cases.order_pizza.order_pizza_use_case import OrderPizzaUseCase
from application.pizza_use_cases.order_pizza.order_pizza_input_dto import OrderPizzaInputDTO
from application.pizza_repo.in_memory_pizza_repo import InMemoryPizzaRepo
from application.pizza_id_generator.integer_pizza_id_generator import IntegerPizzaIdGenerator


def test_get_all_pizzas():
    # Arrange
    pizza_repo = InMemoryPizzaRepo()
    input_dto = OrderPizzaInputDTO(OrderPizzaUseCase.PizzaType.CHEESE)
    order_pizza_use_case = OrderPizzaUseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())
    order_pizza_use_case.execute(input_dto)
    order_pizza_use_case.execute(input_dto)
    order_pizza_use_case.execute(input_dto)
    get_pizza_use_case = GetPizzaUseCase(pizza_repo, LocalClock())

    # Action
    output_dto = get_pizza_use_case.execute()

    # Assert
    assert len(output_dto.pizzas) == 3
