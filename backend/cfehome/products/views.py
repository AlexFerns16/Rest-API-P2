from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.

# create class based view
# -----------------------------------------------------------------
class ProductsCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content = title
        serializer.save(content=content)
        # serializer.save(user=request.user.username)

product_create_view = ProductsCreateAPIView.as_view()


# retrieve (detail) class based view
# -----------------------------------------------------------------
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

product_detail_view = ProductDetailAPIView.as_view()


# list class based view
# -----------------------------------------------------------------
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()


# combined list and create class based view
# -----------------------------------------------------------------
class ProductsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content = title
        serializer.save(content=content)
        # serializer.save(user=request.user.username)

product_list_create_view = ProductsListCreateAPIView.as_view()
