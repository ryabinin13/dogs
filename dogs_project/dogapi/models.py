from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Breed(models.Model):
    """
    Модель породы собаки в бд.

    Атрибуты:
        name: Название породы
        size: Размер породы
        friendliness: Дружелюбие
        trainability: Обучаемость

    """
    SIZE_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    name = models.CharField(max_length=100)
    size = models.CharField(choices=SIZE_CHOICES, default='Medium', max_length=100)
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    shedding_amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exercise_needs = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Dog(models.Model):
    """
    Модель собаки в бд.

    Атрибуты:
        name: Имя собаки
        age: Возраст собаки
        breed: Порода собаки
        gender: Пол собаки
        color: Цвет собаки
        favorite_food: Любимая еда
        favorite_toy: Любимая игрушка

    """
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete = models.CASCADE, related_name='dogs')
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favorite_food = models.CharField(max_length=100)
    favorite_toy = models.CharField(max_length=100)






