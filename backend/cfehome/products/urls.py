from django.urls import path
from products import views

urlpatterns = [
    path('create/', views.product_create_view),
    path('detail/<int:pk>/', views.product_detail_view),
    path('list/', views.product_list_view),
    path('list_create/', views.product_list_create_view),
    path('', views.product_alt_view),
    path('<int:pk>/', views.product_alt_view),
    path('update/<int:pk>/', views.product_update_view),
    path('delete/<int:pk>/', views.product_delete_view),
]
