import json

from django.views import View

from pizza_ordering.core.use_cases.cancel_pizza import CancelPizzaInputDTOFactory
from pizza_ordering.core.use_cases.order_pizza import OrderPizzaInputDTOFactory
from .container import order_pizza_use_case, find_pizza_use_case, cancel_pizza_use_case
from .json_response import json_response




class PizzaController(View):
    def get(self, request):
        output_dto = find_pizza_use_case.execute()
        return json_response(output_dto)

    def post(self, request):
        json_body = json.loads(request.body)
        input_dto = OrderPizzaInputDTOFactory.build(json_body)
        output_dto = order_pizza_use_case.execute(input_dto)
        return json_response(output_dto)

    def put(self, request, pizza_id=None):
        cancel_pizza_input_dto = CancelPizzaInputDTOFactory.build(pizza_id)
        output_dto = cancel_pizza_use_case.execute(cancel_pizza_input_dto)
        return json_response(output_dto)
