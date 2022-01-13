# Create your views here.

from rest_framework import viewsets
from .serializers import RelationshipSerializer, PersonSerializer
from .models import Relationship, Person


class RelationshipView(viewsets.ModelViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer
