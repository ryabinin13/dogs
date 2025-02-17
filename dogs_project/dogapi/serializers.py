from rest_framework import serializers
from .models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    dog_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Breed
        fields = '__all__'

class BreedListSerializer(serializers.ModelSerializer):
    dog_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = ['id', 'name', 'dog_count', 'size', 'friendliness', 'trainability', 'shedding_amount', 'exercise_needs']

class BreedDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability', 'shedding_amount', 'exercise_needs']

class DogSerializer(serializers.ModelSerializer):
    breed_dog_count = serializers.IntegerField(read_only=True)
    breed = BreedSerializer(read_only=True) 
    breed_id = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all(), source='breed', write_only=True)
    class Meta:
        model = Dog
        fields = '__all__'

class DogListSerializer(serializers.ModelSerializer):
    breed_name = serializers.CharField(source='breed.name', read_only=True)
    breed_dog_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'breed_name', 'breed_dog_count', 'color', 'favorite_food', 'favorite_toy', 'gender']

class DogDetailSerializer(serializers.ModelSerializer):
    breed_name = serializers.CharField(source='breed.name', read_only=True)
    breed_avg_age = serializers.FloatField(read_only=True)

    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'breed_name', 'breed_avg_age', 'color', 'favorite_food', 'favorite_toy', 'gender']




