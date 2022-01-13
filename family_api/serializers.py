from rest_framework import serializers
from .models import Relationship,Person

class RelationshipSerializer(serializers.HyperlinkedModelSerializer):
    '''
        序列化 Relationship model
    '''
    
    class Meta:
        model = Relationship
        fields = ('id','name')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    '''
        序列化 Person model 
    '''
    
    class Meta:
        model = Person
        fields = ('id','name','sex','birth_date','intro','relation',)