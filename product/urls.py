from django.urls import path

from product import views
from product.views import ClientUpdateView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('product/', views.product_list, name='product_list'),  # Product list with pagination and search
    path('create/', views.product_create, name='product_create'),  # Create a new product
    path('<int:pk>/update/', views.product_update, name='product_update'),  # Update an existing product
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),  # Delete a product
    path('client/', views.client_list, name='client_list'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('export-products/', views.export_products_to_excel, name='export_products'),
    path('expor-page/', views.exel_page, name='exel_page'),
    path('download-excel/', views.download_excel, name='download_excel'),
]
