from application.clock import LocalClock
from application.pizza_id_generator import IntegerPizzaIdGenerator
from application.pizza_repo import InMemoryPizzaRepo
from application.use_cases import find_pizza, order_pizza


def test_find_all_pizzas():
    # Arrange
    pizza_repo = InMemoryPizzaRepo()
    input_dto = order_pizza.InputDTO("cheese")
    order_pizza_use_case = order_pizza.UseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())
    order_pizza_use_case.execute(input_dto)
    order_pizza_use_case.execute(input_dto)
    order_pizza_use_case.execute(input_dto)
    get_pizza_use_case = find_pizza.UseCase(pizza_repo, LocalClock())

    # Action
    output_dto = get_pizza_use_case.execute()

    # Assert
    assert len(output_dto.pizzas) == 3
