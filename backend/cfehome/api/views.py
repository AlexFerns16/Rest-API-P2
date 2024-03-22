from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def api_home(request, *args, **kwargs):
    
    # url query params (parameters ...?var=val)
    print(request.GET)
    print(request.POST)
    # byte string of json data
    body = request.body
    
    data = {}
    try:
        # string of json data -> python dictionary
        data = json.loads(body)
    except:
        pass
    
    print(data)
    # print(body)
    
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    
    return JsonResponse(data)
