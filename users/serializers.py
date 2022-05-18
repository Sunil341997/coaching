
from rest_framework import serializers
from .models import *
from re import T

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coaches
        fields = ('email', 'name', 'password')

