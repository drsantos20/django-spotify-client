from django.test import TestCase
from ..models import Songs


class SongsTestCase(TestCase):
    def setUp(self):
        Songs.objects.create(title='In the end', artist='Linkin Park')
        Songs.objects.create(title='Great divide', artist='Breaking Benjamin')

    def test_create_songs(self):
        track_a = Songs.objects.get(title='In the end')
        track_b = Songs.objects.get(title='Great divide')
        self.assertEqual(track_a.title, 'In the end')
        self.assertEqual(track_b.title, 'Great divide')
