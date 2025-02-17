from django.urls import include, path
from rest_framework import routers
from .views import DogViewSet, BreedViewSet


router = routers.SimpleRouter()
router.register(r'dogs', DogViewSet, basename='dog')
router.register(r'breeds', BreedViewSet, basename='breed')

urlpatterns = [
    path('', include(router.urls))
]