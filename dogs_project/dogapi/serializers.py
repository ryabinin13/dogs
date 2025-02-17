from rest_framework import serializers
from .models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Breed.

    Включает все поля модели Breed и добавляет поле `dog_count`
    (только для чтения), которое содержит количество собак этой породы.

    Атрибуты:
        dog_count (IntegerField): Количество собак этой породы (только для чтения).

    """
    dog_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Breed
        fields = '__all__'

class BreedListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения списка пород.

    Включает только основные поля модели Breed и добавляет поле
    `dog_count` (только для чтения), которое содержит количество собак этой породы.
    Используется для отображения списка пород с минимальным количеством информации.

    Атрибуты:
        dog_count (IntegerField): Количество собак этой породы (только для чтения).

    """
    dog_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = ['id', 'name', 'dog_count', 'size', 'friendliness', 'trainability', 'shedding_amount', 'exercise_needs']

class BreedDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения подробной информации о породе.

    Включает поля модели Breed, необходимые для отображения детальной информации о породе.

    """
    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability', 'shedding_amount', 'exercise_needs']

class DogSerializer(serializers.ModelSerializer):
     
    """
    Сериализатор для модели Dog.

    Включает все поля модели Dog, а также поле `breed_dog_count`
    (только для чтения), которое содержит количество собак этой породы.

    Поле `breed` сериализуется с использованием `BreedSerializer` (только для чтения).
    Поле `breed_id` используется для записи ID породы.

    Атрибуты:
        breed_dog_count (IntegerField): Количество собак этой породы (только для чтения).
        breed (BreedSerializer): Сериализованное представление породы (только для чтения).
        breed_id (PrimaryKeyRelatedField): ID породы (только для записи).
    """

    breed_dog_count = serializers.IntegerField(read_only=True)
    breed = BreedSerializer(read_only=True) 
    breed_id = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all(), source='breed', write_only=True)
    class Meta:
        model = Dog
        fields = '__all__'

class DogListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения списка собак.

    Включает только основные поля модели Dog и добавляет поле `breed_name`
    (только для чтения), которое содержит имя породы, и поле `breed_dog_count` (только для чтения)
    содержащее количество собак этой породы.

    Атрибуты:
        breed_name (CharField): Имя породы (только для чтения).
        breed_dog_count (IntegerField): Количество собак этой породы (только для чтения).

     """
    breed_name = serializers.CharField(source='breed.name', read_only=True)
    breed_dog_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'breed_name', 'breed_dog_count', 'color', 'favorite_food', 'favorite_toy', 'gender']

class DogDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для отображения подробной информации о собаке.

    Включает поля модели Dog, необходимые для отображения детальной информации о собаке,
    а также поле `breed_name` (только для чтения), которое содержит имя породы, и поле `breed_avg_age` (только для чтения),
    содержащее средний возраст собак этой породы.

    Атрибуты:
        breed_name (CharField): Имя породы (только для чтения).
        breed_avg_age (FloatField): Средний возраст собак этой породы (только для чтения).

    """
    breed_name = serializers.CharField(source='breed.name', read_only=True)
    breed_avg_age = serializers.FloatField(read_only=True)

    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed', 'breed_name', 'breed_avg_age', 'color', 'favorite_food', 'favorite_toy', 'gender']




