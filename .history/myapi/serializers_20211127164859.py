from rest_framework import serializers
from .models import Hero,Company

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    '''
        系列化 Hero model 
    '''
    class Meta:
        model = Hero
        fields = ('id','name','alias')



class CompanySerializer(serializers.HyperlinkedModelSerializer):
    '''
        系列化 Company model 
    '''
    class Meta:
        model = Company
        fields = ('id','name','address','city','official_website')