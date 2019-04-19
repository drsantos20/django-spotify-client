from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ...models import Songs


class TestSongsViewSet(APITestCase):
    client = APIClient()

    @staticmethod
    def create_songs(title='', artist=''):
        if title and artist:
            Songs.objects.create(title=title, artist=artist)

    def setUp(self):
        self.create_songs('Love ve me tender', 'Elvis Presley')
        self.create_songs('Leave all the rest', 'Linkin Park')
        self.create_songs('Dear agony', 'Breaking Benjamin')
        self.create_songs('Last report', 'Papa Roach')
        self.create_songs('Californication', 'Red Hot Chili Peppers')

    def test_get_all_songs(self):
        response = self.client.get(
            reverse('songs-all', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Love ve me tender')
        self.assertEqual(response.data[1]['title'], 'Leave all the rest')
        self.assertEqual(response.data[2]['title'], 'Dear agony')
        self.assertEqual(response.data[3]['title'], 'Last report')
        self.assertEqual(response.data[4]['title'], 'Californication')
