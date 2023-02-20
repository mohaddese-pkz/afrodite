from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import *
from .models import *

class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

class FirstSubCategoryList(generics.ListAPIView):
    serializer_class = FirstSubCategorySerializer
    def get_queryset(self):
        return FirstSubCategory.objects.all()

class SecondSubCategoryList(generics.ListAPIView):
    serializer_class = SecondSubCategorySerializer
    def get_queryset(self):
        return SecondSubCategory.objects.all()

class ThirdSubCategoryList(generics.ListAPIView):
    serializer_class = ThirdSubCategorySerializer
    def get_queryset(self):
        return ThirdSubCategory.objects.all()


class ProductImagesCreate(generics.CreateAPIView):
    serializer_class = ProductImagesSerializer
    queryset = ProductImages.objects.all()


class ProductsList(generics.ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return Products.objects.all()


class ColorsList(generics.ListAPIView):
    serializer_class = ColorsSerializer

    def get_queryset(self):
        return Colors.objects.all()


class CommentsCreate(generics.CreateAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()


class CommentsList(generics.ListAPIView):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        return Comments.objects.all()


class ProductDetails(generics.ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Products.objects.filter(id=id)


class ProductImagesList(generics.ListAPIView):
    serializer_class = ProductImagesSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return ProductImages.objects.filter(product_id=id)


class MotivationDiscountList(generics.ListAPIView):
    serializer_class = MotivationDiscountSerializers
    queryset = MotivationDiscount.objects.all()


class MotivationDiscountUpdate(generics.UpdateAPIView):
    serializer_class = MotivationDiscountSerializers
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    queryset = MotivationDiscount.objects.all()



class ChangeActiveDiscount(generics.UpdateAPIView):
    serializer_class = ProductsSerializer
    permission_classes = [IsAdminUser]
    def update(self, request, *args, **kwargs):
        motivation = MotivationDiscount.objects.filter(id=kwargs['id'], active=True).first()
        if motivation is not None:
            for product in motivation.products.all():
                if product.discount_price == 0:
                    pro = Products.objects.filter(id=product.id).first()
                    pro.discount_price = pro.price - (pro.price * motivation.percentage/100)
                    pro.save()

                else:
                    product.discount_price = 0
                    product.save()

        else:
            return Response({'message': 'motivation not found or is not active'})

        return Response({'message': 'تغییرات اعمال شد'})