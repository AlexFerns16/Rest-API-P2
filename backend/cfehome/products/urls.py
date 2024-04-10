from django.urls import path
from products import views

urlpatterns = [
    
    # class based create
    # -----------------------------------------------------------
    path('create/', views.product_create_view),
    # path('create/', views.product_mixin_view),
    
    # class based detail
    # -----------------------------------------------------------
    path('detail/<int:pk>/', views.product_detail_view, name='product-detail'),
    # path('detail/<int:pk>/', views.product_mixin_view),
    
    # class based list
    # -----------------------------------------------------------
    path('list/', views.product_list_view),
    # path('list/', views.product_mixin_view),
    
    # class based list_create
    # -----------------------------------------------------------
    path('list_create/', views.product_list_create_view, name='product-list-create'),
    
    # class based update
    # -----------------------------------------------------------
    path('update/<int:pk>/', views.product_update_view, name='product-edit'),
    
    # class based delete
    # -----------------------------------------------------------
    path('delete/<int:pk>/', views.product_delete_view),
    
    # function based CRUD
    # -----------------------------------------------------------
    # path('', views.product_alt_view),
    path('<int:pk>/', views.product_alt_view),
]
