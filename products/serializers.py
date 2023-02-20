from rest_framework import serializers
from .models import *

class FirstSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstSubCategory
        fields= '__all__'
class SecondSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondSubCategory
        fields= '__all__'
class ThirdSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdSubCategory
        fields= '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = '__all__'

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class MotivationDiscountSerializers(serializers.ModelSerializer):
    class Meta:
        model = MotivationDiscount
        fields = '__all__'
