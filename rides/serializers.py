# rides/serializers.py

from rest_framework import serializers
from .models import Ride
from django.contrib.auth import get_user_model

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'user', 'start_location', 'end_location', 'created_at']
# installing Customer user
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # This fetches your CustomUser model
        fields = ('id', 'username', 'email', 'role', 'rating')