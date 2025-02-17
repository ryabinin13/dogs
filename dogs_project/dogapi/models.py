from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Breed(models.Model):
    SIZE_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    name = models.CharField()
    size = models.CharField(choices=SIZE_CHOICES, default='Medium')
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    shedding_amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exercise_needs = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Dog(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete = models.CASCADE, related_name='dogs')
    gender = models.CharField()
    color = models.CharField()
    favorite_food = models.CharField()
    favorite_toy = models.CharField()






