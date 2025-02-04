from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import Product
from telegram_bot.models import TelegramUser
from telegram_bot.serializers import TelegramUserSerializer, ProductSerializer


class TelegramBotUserView(ListCreateAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        if TelegramUser.objects.filter(user_id=user_id).exists():
            return Response({"message": "Foydalanuvchi mavjud"}, status=status.HTTP_200_OK)
        return super().create(request, *args, **kwargs)


class ProductDetailView(APIView):
    def get(self, request, serial_number):
        try:
            product = Product.objects.get(serial_number=serial_number)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
