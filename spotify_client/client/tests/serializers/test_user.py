from django.test import TestCase

from ...models.user import User
from ...serializers import UserSerializer


class TestUserSerializer(TestCase):
    def setUp(self):
        self.serializer_data = {
            'email': 'shazam@dc.com',
            'username': 'paul@dc.com'
        }

        self.serializer = UserSerializer(instance=User)

    def test_user_serializer_all(self):
        data = self.serializer_data

        self.assertEqual(data.get('email'), 'shazam@dc.com')
        self.assertEqual(data.get('username'), 'paul@dc.com')


