from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.utils import json
from rest_framework.views import status
from ...models import User


class TestUserViewSet(APITestCase):
    client = APIClient()

    @staticmethod
    def create_songs(email='', username=''):
        if email and username:
            User.objects.create(email=email, username=username)

    def setUp(self):
        self.create_songs(email='shazam@dc.com', username='shazam')
        self.create_songs(email='banner@dc.com', username='banner')
        self.create_songs(email='harley_queen@dc.com', username='harley')
        self.create_songs(email='batman@dc.com', username='batman')

    def test_get_all_users(self):
        response = self.client.get(
            reverse('user-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['email'], 'shazam@dc.com')
        self.assertEqual(response.data[1]['email'], 'banner@dc.com')
        self.assertEqual(response.data[2]['email'], 'harley_queen@dc.com')
        self.assertEqual(response.data[3]['email'], 'batman@dc.com')

    def test_create_users(self):
        data = json.dumps({
            'email': 'wonder@dc.com',
            'username': 'wonder'
        })

        response = self.client.post(
            reverse('user-list', kwargs={'version': 'v1'}),
            data=data,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username='wonder')
        self.assertEqual(response.data, {'email': user.email, 'username': user.username})



