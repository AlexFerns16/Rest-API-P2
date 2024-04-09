from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
from search import client
from rest_framework.response import Response

# Create your views here.

class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        query = request.GET.get('q')
        public = str(request.GET.get('public')) != "0"
        # public = True
        tag = request.GET.get('tag') or None
        print(user, query, public, tag)
        if not query:
            return Response('', status=400)
        results = client.perform_search(query, tags=tag, user=user, public=public)
        print(results)
        return Response(results)


class SearchListOldView(generics.ListAPIView):
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
