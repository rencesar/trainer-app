from django.test import TestCase
from rest_framework.test import APIClient

from model_bakery import baker

from user.models import User


class _TrainerSerializer(TestCase):

    def setUp(self):
        self.user = baker.make(User, is_trainer=True)

    # def test_email_to_me(self):
    #     client = APIClient()
    #     response = client.post('/user/forgot-password/', {'email': self.user.email}, format='json')
    #     self.assertEqual(response.status_code, 204)
