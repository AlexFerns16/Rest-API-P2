from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_create_view),
    path('<int:pk>/', views.product_detail_view),
]
