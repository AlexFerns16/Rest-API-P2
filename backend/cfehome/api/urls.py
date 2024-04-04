from django.urls import path 
from api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    
    # localhost:8000/api/
    path('', views.api_home),
    
    # auth tokens
    path('auth/', obtain_auth_token),
]
