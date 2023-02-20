from rest_framework import serializers
from .models import *

class TicketSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(required=False)
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketMessages
        fields = '__all__'