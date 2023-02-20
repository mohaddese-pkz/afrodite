from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(required=False)
    total_price = serializers.IntegerField(required=False)
    discount_price = serializers.IntegerField(required=False)
    code = serializers.IntegerField(required=False)
    address = serializers.CharField(required=False)
    postal_code = serializers.IntegerField(required=False)
    payment = serializers.CharField(required=False)

    class Meta:
        model = Order
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)
    class Meta:
        model = Discount
        fields = '__all__'