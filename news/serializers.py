from rest_framework import serializers
from .models import NewsEmails, NewsLetterMessage


class NewsEmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsEmails
        fields = '__all__'


class NewsLetterMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetterMessage
        fields = '__all__'