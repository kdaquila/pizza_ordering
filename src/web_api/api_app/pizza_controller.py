from django.http import HttpResponse
from django.views import View
from src.application.clock.local_clock import LocalClock
from src.application.pizza_repo.in_memory_pizza_repo import InMemoryPizzaRepo
from src.application.pizza_id_generator.integer_pizza_id_generator import IntegerPizzaIdGenerator
from src.application.pizza_use_cases.get_all_pizzas.get_pizzas_use_case import GetPizzaUseCase
from src.application.pizza_use_cases.order_pizza.order_pizza_input_dto import OrderPizzaInputDTO
from src.application.pizza_use_cases.order_pizza.order_pizza_use_case import OrderPizzaUseCase
from src.application.pizza_use_cases.order_pizza.order_pizza_input_dto_service import OrderPizzaInputDTOService
from src.application.pizza_use_cases.cancel_pizza.cancel_pizza import CancelPizzaUseCase
from src.application.pizza_use_cases.cancel_pizza.cancel_pizza_input_dto import CancelPizzaInputDTO

import json
import jsonpickle


class PizzaController(View):
    @staticmethod
    def get(request):
        # TODO remove this once database is being used
        pizza_repo = InMemoryPizzaRepo()
        order_pizza_use_case = OrderPizzaUseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())
        pizza_type = OrderPizzaUseCase.PizzaType.CHEESE
        order_pizza_use_case.execute(OrderPizzaInputDTO(pizza_type))
        order_pizza_use_case.execute(OrderPizzaInputDTO(pizza_type))

        # TODO replace this using dependency injection
        get_pizza_use_case = GetPizzaUseCase(pizza_repo, LocalClock())

        output_dto = get_pizza_use_case.execute()
        json_str = jsonpickle.encode(output_dto, unpicklable=False)
        return HttpResponse(json_str)

    @staticmethod
    def post(request):
        json_body = json.loads(request.body)
        input_dto: OrderPizzaInputDTO = OrderPizzaInputDTOService.build_dto(json_body)

        # TODO replace this using dependency injection
        order_pizza_use_case = OrderPizzaUseCase(InMemoryPizzaRepo(), IntegerPizzaIdGenerator(), LocalClock())

        order_pizza_use_case.execute(input_dto)
        return HttpResponse('creating a new pizza order')

    @staticmethod
    def put(request, pizza_id):
        # TODO remove this once database is being used
        pizza_repo = InMemoryPizzaRepo()
        order_pizza_use_case = OrderPizzaUseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())
        pizza_type = OrderPizzaUseCase.PizzaType.CHEESE
        order_pizza_use_case.execute(OrderPizzaInputDTO(pizza_type))

        input_dto = CancelPizzaInputDTO(pizza_id)
        cancel_pizza_use_case = CancelPizzaUseCase(pizza_repo, LocalClock())
        cancel_pizza_use_case.execute(input_dto)
        return HttpResponse(f"canceling pizza order {pizza_id}")
