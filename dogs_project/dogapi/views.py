from rest_framework import viewsets, serializers
from .models import Dog, Breed
from .serializers import BreedDetailSerializer, BreedListSerializer, DogSerializer,DogDetailSerializer, DogListSerializer, BreedSerializer
from django.db.models import Avg, Count, Subquery, OuterRef, FloatField
from django.db.models.functions import Cast


class DogViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления моделью Dog.

    Предоставляет API для создания, чтения, обновления и удаления объектов Dog.
    Разные сериализаторы используются в зависимости от действия:
    - `list`:  `DogListSerializer` для отображения списка собак с основной информацией.
    - `retrieve`: `DogDetailSerializer` для отображения подробной информации о конкретной собаке.
    - `create`, `update`, `partial_update`, `destroy`: `DogSerializer` для операций создания, обновления и удаления.

    get_queryset() переопределен для добавления аннотаций к данным:
    - `list`: аннотируется `breed_dog_count` - общее количество собак каждой породы.
    - `retrieve`: аннотируется `breed_avg_age` - средний возраст собак каждой породы.

    Методы:
        get_queryset():  Переопределяет стандартный queryset для добавления аннотаций.
        get_serializer_class(): Переопределяет стандартный serializer_class в зависимости от текущего действия.
    """

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
    """
    ViewSet для управления моделью Breed.

    Предоставляет API для создания, чтения, обновления и удаления объектов Breed.
    Разные сериализаторы используются в зависимости от действия:
    - `list`: `BreedListSerializer` для отображения списка пород с основной информацией и количеством собак.
    - `retrieve`, `create`, `update`, `partial_update`, `destroy`: `BreedDetailSerializer` для операций чтения, создания, обновления и удаления.

    get_queryset() переопределен для добавления аннотации `dog_count` при получении списка пород.

    Методы:
        get_queryset(): Переопределяет стандартный queryset для добавления аннотации `dog_count`.
        get_serializer_class(): Переопределяет стандартный serializer_class в зависимости от текущего действия.
    """
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
      
    