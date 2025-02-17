from rest_framework import viewsets, serializers
from .models import Dog, Breed
from .serializers import BreedDetailSerializer, BreedListSerializer, DogSerializer,DogDetailSerializer, DogListSerializer, BreedSerializer
from django.db.models import Avg, Count, Subquery, OuterRef, FloatField
from django.db.models.functions import Cast


class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer  

    def get_queryset(self):
        if self.action == 'list':
            breed_dog_count_subquery = Dog.objects.filter(breed_id=OuterRef('breed_id')).values('breed_id').annotate(count=Count('id')).values('count')
            queryset = Dog.objects.all().annotate(breed_dog_count=Subquery(breed_dog_count_subquery))
        elif self.action == 'retrieve':
            breed_avg_age_subquery = Breed.objects.filter(pk=OuterRef('breed_id')).annotate(avg_age=Avg('dogs__age')).values(avg_age=Cast('avg_age', output_field=FloatField()))
            queryset = Dog.objects.all().annotate(breed_avg_age=Subquery(breed_avg_age_subquery))
        else:
            queryset = Dog.objects.all() 
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return DogListSerializer
        elif self.action == 'retrieve':
            return DogDetailSerializer
        return DogSerializer 
    

class BreedViewSet(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    
    def get_queryset(self):
       
        if self.action == 'list':
            queryset = Breed.objects.annotate(dog_count=Count('dogs'))
        else:
            queryset = Breed.objects.all() 
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return BreedListSerializer
        return BreedDetailSerializer
      
    