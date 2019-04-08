from django.test import TestCase
from ...models.user import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email='ribeiro@gmail.com')
        User.objects.create(email='shazam@dc.com')

    def test_create_user(self):
        user_a = User.objects.get(email='ribeiro@gmail.com')
        user_b = User.objects.get(email='shazam@dc.com')
        self.assertEqual(user_a.email, 'ribeiro@gmail.com')
        self.assertEqual(user_b.email, 'shazam@dc.com')
