from django.urls import path 
from api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from products.views import product_list_create_view

urlpatterns = [
    
    # localhost:8000/api/
    path('', views.api_home),
    
    #
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('products/', product_list_create_view, name='product-list'),
    
    # auth tokens
    path('auth/', obtain_auth_token),
]
