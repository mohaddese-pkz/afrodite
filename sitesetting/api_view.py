from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import SiteSettingSerializer
from .models import SiteSetting


class SiteSettingCreate(generics.CreateAPIView):
    serializer_class = SiteSettingSerializer
    permission_classes = [IsAdminUser]
    queryset = SiteSetting.objects.all()


class SiteSettingUpdate(generics.UpdateAPIView):
    serializer_class = SiteSettingSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
    queryset = SiteSetting.objects.all()


class SiteSettingList(generics.ListAPIView):
    serializer_class = SiteSettingSerializer
    queryset = SiteSetting.objects.all()





