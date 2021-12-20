from django.http import HttpResponse
from django.views import View

import json


class PizzaController(View):
    @staticmethod
    def get(request):
        json_str = json.dumps({"message": "getting all pizza orders", "hello": "world", "hi": "there"})
        return HttpResponse(json_str)

    @staticmethod
    def post(request):
        json_body = json.loads(request.body)
        return HttpResponse(f'creating a new pizza order for type {json_body["pizza_type"]}')

    @staticmethod
    def put(request, pizza_id):
        return HttpResponse(f"canceling pizza order {pizza_id}")
