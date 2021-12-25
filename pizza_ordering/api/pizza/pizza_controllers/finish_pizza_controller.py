import json

from django.views import View

from pizza_ordering.core.exceptions import ValidationError, PizzaNotFound, PizzaNotCooking
from pizza.container import finish_pizza_use_case
from pizza.json_response import json_response


class FinishPizzaController(View):
    def put(self, request, pizza_id=None):
        """
        This handles the route PUT /api/pizza/<int:id>/cancel. It cancels the given pizza.
        :param request:
        :param pizza_id:
        :return:
        """
        response_obj = {"status": "",
                        "message": "",
                        "data": None}
        try:
            if pizza_id is None:
                raise ValidationError("Pizza type is required")
            finish_pizza_use_case.execute(pizza_id)
            response_obj["status"] = "success"

        except (PizzaNotFound, PizzaNotCooking) as err:
            response_obj["status"] = "fail"
            response_obj["message"] = str(err)

        except Exception as err:
            response_obj["status"] = "error"
            response_obj["message"] = "Internal server error"

        return json_response(response_obj)
