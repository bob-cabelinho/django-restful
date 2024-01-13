from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ProductDetailAPIView(generics.RetrieveAPIView):
    '''
        Class to request [GET] a single product.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    '''
        Class to request [POST] a product.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        price = serializer.validated_data.get("price")
        description = serializer.validated_data.get("description") or None
        if description is None:
            description = title
        serializer.save()

class ProductListCreateAPIView(generics.ListCreateAPIView):
    '''
        Class to request [GET] a list products.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        price = serializer.validated_data.get("price")
        description = serializer.validated_data.get("description") or None
        if description is None:
            description = title
        serializer.save(description=description)

class ProductUpdateAPIView(generics.UpdateAPIView):
    '''
        Class to request [UPDATE] a single product.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.description:
            instance.description = instance.title

class ProductDeleteAPIView(generics.DestroyAPIView):
    '''
        Class to request [DELETE] a single product.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        

@api_view(["GET", "POST"])
def productAltView(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:                                  # Detail Product View
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data  # List Products View

    if method == "POST":
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            price = serializer.validated_data.get("price")
            serializer.save()
    
    if method == "DELETE":
        serializer = ProductSerializer(data=request.data)
