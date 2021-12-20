from django.http import HttpResponse
from django.views import View
from application.clock import LocalClock
from application.pizza_repo import InMemoryPizzaRepo
from application.pizza_id_generator import IntegerPizzaIdGenerator
from application.use_cases import cancel_pizza, find_pizza, order_pizza

import json
import jsonpickle


class PizzaController(View):
    def get(self, request):
        # TODO remove this once database is being used
        pizza_repo = InMemoryPizzaRepo()
        order_pizza_use_case = order_pizza.UseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())
        input_dto = order_pizza.InputDTOFactory.build({"pizza_type": "cheese"})
        order_pizza_use_case.execute(input_dto)
        order_pizza_use_case.execute(input_dto)

        # TODO replace this using dependency injection
        find_pizza_use_case = find_pizza.UseCase(pizza_repo, LocalClock())

        output_dto = find_pizza_use_case.execute()
        json_str = jsonpickle.encode(output_dto, unpicklable=False)
        return HttpResponse(json_str)

    def post(self, request):
        json_body = json.loads(request.body)
        input_dto = order_pizza.InputDTOFactory.build(json_body)

        # TODO replace this using dependency injection
        order_pizza_use_case = order_pizza.UseCase(InMemoryPizzaRepo(), IntegerPizzaIdGenerator(), LocalClock())

        output_dto = order_pizza_use_case.execute(input_dto)
        json_str = jsonpickle.encode(output_dto, unpicklable=False)
        return HttpResponse(json_str)

    def put(self, request, pizza_id):
        # TODO remove this once database is being used
        pizza_repo = InMemoryPizzaRepo()
        order_pizza_use_case = order_pizza.UseCase(pizza_repo, IntegerPizzaIdGenerator(), LocalClock())
        order_pizza_input_dto = order_pizza.InputDTOFactory.build({"pizza_type": "cheese"})
        order_pizza_use_case.execute(order_pizza_input_dto)

        cancel_pizza_use_case = cancel_pizza.UseCase(pizza_repo, LocalClock())
        output_dto = cancel_pizza_use_case.execute(cancel_pizza.InputDTO(pizza_id))
        json_str = jsonpickle.encode(output_dto, unpicklable=False)
        return HttpResponse(json_str)
