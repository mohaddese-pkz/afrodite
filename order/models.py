from django.db import models
from products.models import Products
from django.contrib.auth.models import User


class Order(models.Model):
    pursuit_choises = (
        ('waitting', 'در وضعیت انتظار'),
        ('register', 'ثبت شده'),
        ('confirm', 'تایید شده'),
        ('sent', 'ارسال شده'),
        ('received', 'توسط مشتری دریافت شده'),
    )
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='product')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    address = models.TextField(verbose_name='address')
    postal_code = models.IntegerField(verbose_name='postal_code')
    count = models.IntegerField(verbose_name='count')
    price = models.IntegerField(verbose_name='price')
    discount_price = models.IntegerField(verbose_name='discount_price')
    total_price = models.IntegerField(verbose_name='total_price')
    code = models.IntegerField(verbose_name='code')
    tracking_code = models.IntegerField(default=0, verbose_name='tracking_code')
    discount = models.IntegerField(verbose_name='discount')
    create_payment_date = models.DateTimeField(auto_now_add=True, verbose_name='create_payment_date')
    modified_payment_date = models.DateTimeField(auto_now=True, verbose_name='modified_payment_date')
    payment_status = models.BooleanField(default=False, verbose_name='payment_status')
    pursuit = models.CharField(max_length=233, choices=pursuit_choises, null=True, blank=True, verbose_name='pursuit')
    is_gift = models.BooleanField(null=True, blank=True, default=False, verbose_name='is_gift')
    payment = models.CharField(max_length=999, verbose_name='payment')


class Discount(models.Model):
    name = models.CharField(max_length=999, verbose_name='name')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='product')
    amount = models.IntegerField(verbose_name='amount')
    count = models.IntegerField(verbose_name='count')
    date = models.DateTimeField(auto_now=True, verbose_name='date')
    percentage = models.IntegerField(verbose_name='percentage')
    is_active = models.BooleanField(default=True, verbose_name='is_active')
