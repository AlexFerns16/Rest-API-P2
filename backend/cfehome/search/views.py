from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.

class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self, *args, **kwargs):
        print(Product)
        qs = super().get_queryset(*args, **kwargs)
        print(super()) # <super: <class 'SearchListView'>, <SearchListView object>>
        print(qs) # get's the query from 'queryset' and gives the result of 'Product.objects.all()'
        q = self.request.GET.get('q')
        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
            # results = Product.objects.search(q, user=user) # alternative 
        return results
