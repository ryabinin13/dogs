from django.urls import include, path
from rest_framework import routers
from .views import BreedViewSet


router = routers.SimpleRouter()
router.register(r'breeds', BreedViewSet, basename='breed')

urlpatterns = [
    path('', include(router.urls))
]