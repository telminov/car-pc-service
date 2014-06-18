# coding: utf-8
import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder

def json_response(data, status=200):
    data_json = json.dumps(data, cls=DjangoJSONEncoder)
    return HttpResponse(data_json, content_type='application/json', status=status)
