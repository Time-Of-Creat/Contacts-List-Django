from django.test import TestCase
from django.contrib.auth.models import User


class ContactModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )
        
        self.contact_data = {
            'first_name': 'Иван',
            'last_name': 'Петров',
            "phone_number": "+70000000000",
            "email": "test@test.tst"
        }