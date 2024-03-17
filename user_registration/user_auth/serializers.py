from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializer class for the user model"""
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']