from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
import json

# Create your views here.

# -----------------------------------------------------------------
# def api_home(request, *args, **kwargs):
    
#     # url query params (parameters ...?var=val)
#     print(request.GET)
#     print(request.POST)

#     # byte string of json data
#     body = request.body
    
#     data = {}
#     try:
#         # string of json data -> python dictionary
#         data = json.loads(body)
#     except:
#         pass
    
#     print(data)
#     # print(body)
    
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
    
#     return JsonResponse(data)


# -----------------------------------------------------------------
@api_view()
def api_home(request, *args, **kwargs):
    """ 
    DRF API View
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
        print(request.body)
        return Response(data)
