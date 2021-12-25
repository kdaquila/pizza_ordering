import json

from django.views import View

from pizza_ordering.core.exceptions import ValidationError, PizzaNotFound, CannotCancelPizza
from pizza.container import order_pizza_use_case, find_pizza_use_case
from pizza.json_response import json_response


class PizzaController(View):
    def get(self, request):
        """
        This handles the route GET /api/pizza. It will return all pizzas.
        :param request:
        :return:
        """
        response_obj = {"status": "",
                        "message": "",
                        "data": None}
        try:
            response_obj["status"] = "success"
            response_obj["data"] = find_pizza_use_case.execute()

        except Exception as err:
            response_obj["status"] = "error"

        return json_response(response_obj)

    def post(self, request):
        """
        This handles the route POST /api/pizza. It allows a pizza to be ordered.
        :param request:
        :return:
        """
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
            response_obj["status"] = "fail"
            response_obj["message"] = str(err)

        except Exception as err:
            response_obj["status"] = "error"
            response_obj["message"] = "Internal server error"

        return json_response(response_obj)
