from rest_framework import viewsets, serializers
from .models import Breed
from .serializers import BreedDetailSerializer, BreedListSerializer, BreedSerializer
from django.db.models import Avg, Count, Subquery, OuterRef, FloatField
from django.db.models.functions import Cast


class BreedViewSet(viewsets.ModelViewSet):
    serializer_class = BreedSerializer # Default serializer
    
    def get_queryset(self):
       
        if self.action == 'list':
            queryset = Breed.objects.annotate(dog_count=Count('dogs'))
        else:
            queryset = Breed.objects.all()  # No annotation for detail view
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return BreedListSerializer
        return BreedDetailSerializer