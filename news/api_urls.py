from django.urls import path
from . import api_view



urlpatterns = [
    path('email/create/', api_view.NewsLetterEmailCreate.as_view(), name='NewsLetterEmailCreate'),
    path('email/list/', api_view.NewsLetterEmailList.as_view(), name='NewsLetterEmailList'),
    path('create/', api_view.NewsLetterCreate.as_view(), name='NewsLetterCreate'),
    path('list/', api_view.NewsLetterList.as_view(), name='NewsLetterList'),
    path('update/<int:id>', api_view.UpdateNewsLetters.as_view(), name='UpdateNewsLetters'),
    path('sendmail/', api_view.SendEmail, name='SendEmail'),

]