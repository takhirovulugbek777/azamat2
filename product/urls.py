from django.urls import path

from product import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('product/', views.product_list, name='product_list'),  # Product list with pagination and search
    path('create/', views.product_create, name='product_create'),  # Create a new product
    path('<int:pk>/update/', views.product_update, name='product_update'),  # Update an existing product
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),  # Delete a product
    path('client/', views.client_list, name='client_list'),
]
