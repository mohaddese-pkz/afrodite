from rest_framework import serializers
from .models import *


class WholeBuyerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WholeBuyerUser
        fields = '__all__'


class SettelMentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettleMent
        fields = '__all__'