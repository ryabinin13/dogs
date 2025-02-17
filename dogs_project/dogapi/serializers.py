from rest_framework import serializers
from .models import Breed


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