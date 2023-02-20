from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class UserCreate(generics.CreateAPIView):

    # create new user

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class UserList(generics.ListAPIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        return Profile.objects.all()



class UserUpdate(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]
    queryset = Profile.objects.all()
    lookup_field = 'id'


class UserDelete(generics.DestroyAPIView):
    """
        Delete  Comment With  Comment Id
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]
    queryset = Profile.objects.all()
    lookup_field = 'id'



