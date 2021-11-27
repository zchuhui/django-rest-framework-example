from rest_framework import serializers
from .models import Hero

# 系列化 Hero model 
class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('id','name','alias')