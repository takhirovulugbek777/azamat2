from django.urls import path

from telegram_bot import views
from telegram_bot.views import ProductDetailView

urlpatterns = [
    path('users/', views.TelegramBotUserView.as_view(), name='telegram_bot'),
    path('products/<str:serial_number>/', ProductDetailView.as_view(), name='product-detail'),
]
