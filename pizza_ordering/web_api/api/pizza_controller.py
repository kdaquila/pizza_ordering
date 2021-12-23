import json

from django.views import View

from pizza_ordering.core.exceptions import ValidationError
from pizza_ordering.core.use_cases.cancel_pizza import CancelPizzaInputDTOFactory
from .container import order_pizza_use_case, find_pizza_use_case, cancel_pizza_use_case
from .json_response import json_response


class PizzaController(View):
    def get(self, request):
        output_dto = find_pizza_use_case.execute()
        return json_response(output_dto)

    def post(self, request):
        response_obj = {"status": "",
                        "message": "",
                        "data": None}
        try:
            input_dict = json.loads(request.body)
            pizza_type = input_dict.get("pizza_type")
            if pizza_type is None:
                raise ValidationError("Pizza type is required")

            response_obj["data"] = order_pizza_use_case.execute(pizza_type)
            response_obj["status"] = "success"

        except ValidationError as err:
            response_obj["status"] = "fail",
            response_obj["message"] = str(err)

        except Exception:
            response_obj["status"] = "error",
            response_obj["message"] = "Internal server error"

        return json_response(response_obj)

    def put(self, request, pizza_id=None):
        cancel_pizza_input_dto = CancelPizzaInputDTOFactory.build(pizza_id)
        output_dto = cancel_pizza_use_case.execute(cancel_pizza_input_dto)
        return json_response(output_dto)
