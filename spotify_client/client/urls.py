from django.urls import path
from .viewsets import SongsViewSet


urlpatterns = [
    path('songs/', SongsViewSet.as_view({'get': 'list'}), name="songs-all")
]
