from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .viewsets import SongsViewSet
from .viewsets import UserViewSet

router = routers.SimpleRouter()

router.register(r'songs', SongsViewSet, base_name='songs')
router.register(r'user', UserViewSet, base_name='user')

urlpatterns = [
    url(r'^', include(router.urls)),
]
