from django.urls import path
from .api_view import *


urlpatterns = [
  path("get-details/", UserDetailAPI.as_view(), name='UserDetailAPI'),
  path('register/', RegisterUserAPIView.as_view(), name='RegisterUserAPIView'),
  path('change-password/', ChangePasswordView.as_view(), name='change-password'),
  path('login/', LoginAPI.as_view(), name='LoginAPI'),
  path('reset/confirm/', confirmPassword, name='confirmPassword'),
  # path('reset/confirm/init-alpine.js', Js, name='Js'),
  # path('reset/confirm/tailwind.output.css', Css, name='Css'),
  # path('reset/confirm/assets/img/forgot-password-office.jpeg', forgotpasswordoffice, name='Css'),
  # path('reset/confirm/assets/img/forgot-password-office-dark.jpeg', forgotpasswordofficedark, name='Css'),
]