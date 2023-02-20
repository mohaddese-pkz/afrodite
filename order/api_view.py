from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
import random
from .serializers import *
from .models import *
from products.models import Products
from customaccount.models import Profile
from sitesetting.models import CountPrize




class CreateOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = OrderSerializer(data=request.data)

        if data.is_valid():
            product_id = data.data.get('product')
            product = Products.objects.filter(id=product_id).first()

            if product is not None:
                count = data.data.get('count')
                store = product.store
                if count >= store:
                    return Response({'message': 'موجودی کالا ناکافی است'})
                else:
                    product.store = store-count
                    product.save()
                user_id = self.request.user.id
                is_gift = data.data.get('is_gift')
                if is_gift == True:
                    address = request.data.get('address')
                    postal_code = request.data.get('postal_code')
                    if address is None or postal_code is None:
                        return Response({'message': 'آدرس و کدپستی مورد نظر خود را وارد کنید.'})

                else:
                    profile = Profile.objects.filter(user_id=user_id).first()
                    address = profile.address
                    postal_code = profile.postal_code

                orders = Order.objects.filter(user_id=user_id, payment_status=False).all()

                product_history = Order.objects.filter(user_id=user_id, product_id=product_id, payment_status=False).first()
                if product_history:
                    product_history.delete()

                percentage = 0
                prizes = CountPrize.objects.all()

                for prize in prizes:

                    if count >= prize.min_count and count < prize.max_count:
                        percentage = prize.percentage

                if product.discount_price == 0:
                    price = product.price * (100-percentage) * count
                else:
                    price = product.discount_price * (100-percentage) * count

                order = Order.objects.filter(user_id=request.user.id, payment_status=False).first()
                if order:
                    code = order.code
                else:

                    flag = 0
                    code = 0
                    while flag != 1:
                        code = random.randint(10000, 100000)
                        check = Order.objects.filter(code=code).first()
                        if check == None:
                            flag = 1

                if orders.first() is None:

                    Order.objects.create(user_id=user_id, product_id=product_id, count=count, price=price, discount_price=price, total_price=price, code=code, discount=data.data.get('discount'), address=address, postal_code=postal_code, is_gift=is_gift, payment='none', pursuit='waitting')


                else:

                    total_price = price
                    for order in orders:
                        total_price += order.price

                    Order.objects.create(user_id=user_id, product_id=product_id, count=count, price=price, discount_price=total_price, total_price=total_price, code=code, discount=data.data.get('discount'), address=address, postal_code=postal_code, is_gift=is_gift, payment='none', pursuit='waitting')


                return Response({'message': 'سفارش خرید ثبت شد.'})

            else:
                return Response({'message': 'محصولی وجود ندارد.'})

        else:
            return Response(data.errors)



class RegisterDiscount(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    def update(self, request, *args, **kwargs):
        orders = Order.objects.filter(user_id=request.user.id, payment_status=False).all()
        discountC = Discount.objects.filter(name=request.data.get('name'), is_active=True).first()
        discount_amount = 0
        if orders and discountC:
            product_id = discountC.product.id
            for order in orders:
                if order.product.id == product_id:
                    if order.count >= discountC.count and order.price <= discountC.amount:
                        discount = discountC.percentage

                    else:
                        discount = 0

                    if order.product.discount_price == 0:
                        discount_amount += order.product.price * order.count
                    else:
                        discount_amount += order.product.discount_price * order.count


                    user_id = request.user.id
                    order = Order.objects.filter(user_id=user_id, payment_status=False).last()
                    discount_price = order.total_price - discount_amount
                    order.discount_price = discount_price
                    order.save()

                    return Response({'message': ' کد تخفیف اعمال شد. '})

        else:
            return Response({'message': 'not found'})





class DeleteOrder(generics.DestroyAPIView):
    serializer_class = OrderSerializer

    def delete(self, request, *args, **kwargs):
        order = Order.objects.filter(user_id=request.user.id, id=kwargs['id']).first()
        if order is not None:
            order.delete()
            return Response({'message': 'سفارش حذف شد'})

        else:
            return Response({'message': 'not found'})



class DiscountList(generics.ListAPIView):
    serializer_class = DiscountSerializer
    permission_classes = [IsAdminUser]
    queryset = Discount.objects.all()

