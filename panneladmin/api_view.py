import datetime, requests
from jalali_date import date2jalali
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import APIView
from auth.serializers import UserSerializer
from django.contrib.auth.models import User
from ticket.serializers import TicketSerializer, TicketMessagesSerializer
from ticket.models import Ticket, TicketMessages
from customaccount.serializers import ProfileSerializer
from customaccount.models import Profile
from .serializer import *
from .models import SettleMent
from order.serializers import DiscountSerializer, OrderSerializer
from order.models import Discount, Order
from config.settings import API_KEY


class UserList(generics.ListAPIView):
  serializer_class = UserSerializer
  permission_classes = [IsAdminUser]
  queryset = User.objects.all()



class TicketList(generics.ListAPIView):
  serializer_class = TicketSerializer
  permission_classes = [IsAdminUser]
  queryset = Ticket.objects.all()



class TicketMessagesList(generics.ListAPIView):
  serializer_class = TicketMessagesSerializer

  def get_queryset(self):
    id = self.kwargs['id']
    return TicketMessages.objects.filter(ticket_id=id)


class Is_Whole(generics.CreateAPIView):

  serializer_class = WholeBuyerUserSerializer
  permission_classes = [IsAdminUser]

  def create(self, request, *args, **kwargs):
    id = self.kwargs['id']
    Is_WholeBuyer = self.request.POST.get('Is_WholeBuyer')
    WholeBuyerUser.objects.create(user_id=id, Is_WholeBuyer=Is_WholeBuyer)
    return Response({'message': 'وضعیت کاربر ثبت شد.'})



class BirthDayList(generics.ListAPIView):
  serializer_class = ProfileSerializer
  permission_classes = [IsAdminUser]

  def get_queryset(self):

    today_date = datetime.date.today()
    jalali_today_date = date2jalali(today_date)
    users = Profile.objects.filter(birthday__month=jalali_today_date.month, birthday__day=jalali_today_date.day).all()
    return users


class SettelMentList(generics.ListAPIView):
  serializer_class = SettelMentSerializer
  permission_classes = [IsAdminUser]
  queryset = SettleMent.objects.all()



class CreateDiscount(generics.CreateAPIView):
  serializer_class = DiscountSerializer
  permission_classes = [IsAdminUser]
  queryset = Discount.objects.all()


def SendDiscountSms(receptor, token, token2, token3):
  url = f'https://api.kavenegar.com/v1/{API_KEY}/verify/lookup.json'
  data = {
      'receptor': receptor,
      'token': token,
      'token2': token2,
      'token3': token3,
      'template': 'DiscountAfrodite'
    }
  res = requests.post(url, data)
  print(f'token: {token}, send to: {receptor}')

class SendDiscountSmsC(APIView):
  def post(self):
    user = self.request.data.get('user')
    profile = Profile.objects.filter(user_id=user).first()
    discounts = Discount.objects.filter(is_active=True).all()
    if discounts:
      for discount in discounts:
        discount_name = discount.name
        discount_percentage = discount.percentage
        discount_product = discount.product.name
        if profile:
          SendDiscountSms(profile.phone_number, discount_percentage, discount_product, discount_name)

        else:
          return Response({'message': 'کاربر پروفایل خود را تکمیل نکرده است'})

    else:
      return Response({'message': 'کد تخفیف فعالی وجود ندارد.'})


class ChangePursuit(generics.UpdateAPIView):
  permission_classes = [IsAdminUser]
  serializer_class = OrderSerializer
  lookup_field = 'id'
  queryset = Order
  
  
  
class OrderLists(generics.ListAPIView):
  permission_classes = [IsAdminUser]
  serializer_class = OrderSerializer
  queryset = Order.objects.all()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
