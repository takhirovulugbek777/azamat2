from rest_framework.serializers import ModelSerializer

from product.models import Product
from .models import TelegramUser


class TelegramUserSerializer(ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'