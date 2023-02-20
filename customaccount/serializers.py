from .models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    Image = serializers.ImageField(required=False)

    class Meta:
        model = Profile
        fields = '__all__'

        