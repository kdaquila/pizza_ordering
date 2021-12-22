import json

import jsonpickle
from django.http import HttpResponse
from django.views import View

from core.use_cases.cancel_pizza import CancelPizzaInputDTOFactory
from core.use_cases.order_pizza import OrderPizzaInputDTOFactory
from .container import order_pizza_use_case, find_pizza_use_case, cancel_pizza_use_case


class PizzaController(View):
    def get(self, request):
        output_dto = find_pizza_use_case.execute()

        json_str = jsonpickle.encode(output_dto, unpicklable=False)
        return HttpResponse(json_str)

    def post(self, request):
        json_body = json.loads(request.body)
        input_dto = OrderPizzaInputDTOFactory.build(json_body)

        output_dto = order_pizza_use_case.execute(input_dto)

        json_str = jsonpickle.encode(output_dto, unpicklable=False)
        return HttpResponse(json_str)

    def put(self, request, pizza_id):
        cancel_pizza_input_dto = CancelPizzaInputDTOFactory.build(pizza_id)

        output_dto = cancel_pizza_use_case.execute(cancel_pizza_input_dto)

        json_str = jsonpickle.encode(output_dto, unpicklable=False)
        return HttpResponse(json_str)
