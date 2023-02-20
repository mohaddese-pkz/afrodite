from django.urls import path
from . import api_view


urlpatterns = [
    path('create/', api_view.CreateOrder.as_view(), name='CreateOrder'),
    path('register/discount/', api_view.RegisterDiscount.as_view(), name='RegisterDiscount'),
    path('delete/<int:id>', api_view.DeleteOrder.as_view(), name='DeleteOrder'),
    path('discount/', api_view.DiscountList.as_view(), name='DiscountList'),
]


