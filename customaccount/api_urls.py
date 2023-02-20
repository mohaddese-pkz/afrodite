from django.urls import path
from . import api_view

urlpatterns = [
    path('create/', api_view.UserCreate.as_view(), name='UserCreate'),
    path('list/', api_view.UserList.as_view(), name='UserList'),
    path('update/<int:id>', api_view.UserUpdate.as_view(), name='UserUpdate'),
    path('delete/<int:id>', api_view.UserDelete.as_view(), name='UserDelete'),
]
