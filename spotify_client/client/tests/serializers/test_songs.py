from django.test import TestCase

from ...models.songs import Songs
from ...serializers import SongsSerializer


class TestSongsSerializer(TestCase):
    def setUp(self):
        self.serializer_data = {
            'tittle': 'In the end',
            'artist': 'Linkin Park'
        }
        self.serializer = SongsSerializer(instance=Songs)

    def test_user_serializer_all(self):
        data = self.serializer_data

        self.assertEqual(data.get('tittle'), 'In the end')
        self.assertEqual(data.get('artist'), 'Linkin Park')
