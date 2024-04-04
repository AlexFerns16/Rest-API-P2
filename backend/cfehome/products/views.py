from django.shortcuts import render
from rest_framework import authentication, generics, mixins, permissions
from products.models import Product
from products.permissions import IsStaffEditorPermission
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import Http404

# Create your views here.

# mixins
# -----------------------------------------------------------------
class ProductMixinView(
        mixins.CreateModelMixin,            # create
        mixins.ListModelMixin,              # list
        mixins.RetrieveModelMixin,          # detail
        generics.GenericAPIView             # generic
    ):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    # list and detail
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            # detail
            return self.retrieve(request, *args, **kwargs)
        # list
        return self.list(request, *args, **kwargs)
    
    # create
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    # for create
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content = "this is a single view doing a cool stuff"
        serializer.save(content=content)
        # serializer.save(user=request.user.username)

product_mixin_view = ProductMixinView.as_view()


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


# update class based view
# -----------------------------------------------------------------
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()


# delete class based view
# -----------------------------------------------------------------
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

product_delete_view = ProductDestroyAPIView.as_view()


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
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.DjangoModelPermissions]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = title
        serializer.save(content=content)
        # serializer.save(user=request.user.username)

product_list_create_view = ProductsListCreateAPIView.as_view()


# function based view
# -----------------------------------------------------------------
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    
    if request.method == 'GET':
       
        # detail view
        if pk is not None:
            
            # method 1
            # obj = Product.objects.get(pk=pk)
            # if not obj.exists():
            #     raise Http404()
            # else:
            #     data = ProductSerializer(obj, many=False).data
            
            # method 2
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
             
            return Response(data)
        
        # list view
        else:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)

    if request.method == 'POST':
        
        # create view
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
