from django.test import TestCase

from ...models.user import User
from ...serializers import UserSerializer


class TestUserSerializer(TestCase):
    def setUp(self):
        self.user_serializer = {
            'email': 'drsantos20@gmail.com'
        }

        self.serializer_data = {
            'email': 'shazam@dc.com'
        }

        self.user = User.objets.create(**self.user_serializer)
        self.serializer = UserSerializer(instance=self.user)


