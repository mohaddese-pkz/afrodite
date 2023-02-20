from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework import status
from .serializers import ChangePasswordSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.dispatch import receiver
from kavenegar import *
from customaccount.models import Profile
from config.settings import API_KEY


# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)



#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer



# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)



class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def SendSms(receptor, token):
    url = f'https://api.kavenegar.com/v1/{API_KEY}/verify/lookup.json'
    data = {
        'receptor': receptor,
        'token': token,
        'template': 'forgetpasswordAfrodite'
    }
    res = requests.post(url, data)
    print(f'token: {token}, send to: {receptor}')



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):


    plaintext_message = "http://127.0.0.1:8000{}confirm/?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    # plaintext_message = 2345
    send_mail(
        # title:
        "Password Reset for {title}".format(title="afrodite"),
        # message:
        plaintext_message,
        # from:
        "mohaddese.pakzaban@gmail.com",
        # to:
        [reset_password_token.user.email]
        )
    profile = Profile.objects.filter(user=reset_password_token.user).first()
    if profile:
        SendSms(profile.phone_number, plaintext_message)



def confirmPassword(request):
    token = request.GET.get('token')
    return render(request, 'auth/reset/confirm/password_reset_done.html')

