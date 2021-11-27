from rest_framework import serializers
from .models import Hero

class HeroSerializer(serializers.HyperfineSerializer):
    class Meta:
        model = Hero
        fields = ('name','alias')