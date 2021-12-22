import jsonpickle
from django.http import HttpResponse


def json_response(data):
    return HttpResponse(jsonpickle.encode(data, unpicklable=False))
