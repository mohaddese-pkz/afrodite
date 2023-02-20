from django.urls import path
from . import api_view

urlpatterns = [
    path('user/list/', api_view.UserList.as_view(), name='UserList'),
    path('ticket/list/', api_view.TicketList.as_view(), name='ticket_list'),
    path('list/message/<int:id>', api_view.TicketMessagesList.as_view(), name='ticket_list_message'),
    path('whole/<int:id>', api_view.Is_Whole.as_view(), name='Is_Whole'),
    path('birthdays/', api_view.BirthDayList.as_view(), name='BirthDayList'),
    path('settelment/', api_view.SettelMentList.as_view(), name='SettelMentList'),
    path('create/discount/', api_view.CreateDiscount.as_view(), name='CreateDiscount'),
    path('discount/sms/', api_view.SendDiscountSmsC.as_view(), name='SendDiscountSmsC'),
    path('order/pursuit/<int:id>', api_view.ChangePursuit.as_view(), name='ChangePursuit'),
    path('order/list/', api_view.OrderLists.as_view(), name='OrderLists'),
]