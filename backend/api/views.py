import json
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import JsonResponse

from products.models import Product
from products.serializers import ProductSerializer

def api_home(request):
    '''
    
    '''
    body = request.body                                 # Byte string of JSON Request
    data = {}                                           # Payload data for response

    try:
        data = json.loads(body)                         # Tranform JSON to dict()
        data["params"] = request.GET                    # Get "params" from request
        data["headers"] = dict(request.headers)         # Get "headers" from request and serialize it
        data["content_type"] = request.content_type
    except:
        pass

    return JsonResponse(data)

@api_view(['POST'])                                     # Decorator REST Framework
def api_home(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return Response(serializer.data)
    return Response({"Invalid Value"} ,status=400)
