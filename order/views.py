from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import json
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from .models import Order
from datetime import date
from panneladmin.models import SettleMent
from config.settings import API_KEY
from customaccount.models import Profile


MERCHANT = f'cce85bdd-9845-4e11-b313-d933eda3a975'
# MERCHANT = f'92fbb122-2393-4b29-937c-06af7b8c7659'
# ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
# ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
# ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
ZP_API_REQUEST = 'https://sandbox.zarinpal.com/pg/v4/payment/request.json'
ZP_API_VERIFY = 'https://sandbox.zarinpal.com/pg/v4/payment/verify.json'
ZP_API_STARTPAY = 'https://sandbox.zarinpal.com/pg/StartPay/'


#amount = 11000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = f'mohaddese.pakzaban@gmail.com'  # Optional
mobile = f'09134568897'  # Optional
# Important: need to edit for realy server.
CallbackURL = f'http://127.0.1:8000/order/payment/verify/' #ALLOWED_HOSTS[0]


def SendOrderSms(receptor, token, token2):
    url = f'https://api.kavenegar.com/v1/{API_KEY}/verify/lookup.json'
    data = {
        'receptor': receptor,
        'token': token,
        'token2': token2,
        'template': 'paymentThanksAfrodite'
    }
    res = requests.post(url, data)
    print(f'token: {token}, send to: {receptor}')


def send_request(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(user_id=request.user.id, payment_status=False).last()
        global amount

        amount = order.discount_price
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "callback_url": CallbackURL,
            "description": description,
            "metadata": {"mobile": mobile, "email": email}
        }
        req_header = {"accept": "application/json", "content-type": "application/json'"}
        req = requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
        authority = req.json()['data']['authority']
        if len(req.json()['errors']) == 0:
            return redirect(ZP_API_STARTPAY.format(authority=authority))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        return redirect('/')



def verify(request):

    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json", "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']

            if t_status == 100:
                products = Order.objects.filter(user_id=request.user.id, payment_status=False).all()

                for p in products:
                    p.payment_status = True
                    p.tracking_code = req.json()['data']['ref_id']
                    p.payment = 'Transaction success'
                    p.save()
                    code = p.code
                SettleMent.objects.create(user_id=request.user.id, amount=amount)

                profile = Profile.objects.filter(user_id=request.user.id).first()
                SendOrderSms(profile.phone_number, code, req.json()['data']['ref_id'])

                return HttpResponse('Transaction success.\nRefID: ' + str(req.json()['data']['ref_id']))

            elif t_status == 101:
                products = Order.objects.filter(user_id=request.user.id, payment_status=False).all()

                for p in products:
                    p.tracking_code = req.json()['data']['ref_id']
                    p.payment = 'Transaction submitted : ' + str(req.json()['data']['message'])
                    p.save()
                return HttpResponse('Transaction submitted : ' + str(req.json()['data']['message']))

            else:
                products = Order.objects.filter(user_id=request.user.id, payment_status=False).all()

                for p in products:
                    p.tracking_code = req.json()['data']['ref_id']
                    p.payment = 'Transaction failed.\nStatus: ' + str(req.json()['data']['message'])
                    p.save()
                return HttpResponse('Transaction failed.\nStatus: ' + str(req.json()['data']['message']))

        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            products = Order.objects.filter(user_id=request.user.id, payment_status=False).all()

            for p in products:
                p.tracking_code = req.json()['errors']['code']
                p.payment = f"Error code: {e_code}, Error Message: {e_message}"
                p.save()
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")

    else:
        products = Order.objects.filter(user_id=request.user.id, payment_status=False).all()

        for p in products:
            p.payment = 'Transaction failed or canceled by user'
            p.save()

        return HttpResponse('Transaction failed or canceled by user')

