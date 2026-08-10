from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Contact


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
            "email": "test@test.tst",
            'user': self.user
        }
    
    def testCreateUser(self):
        contact = Contact.objects.create(**self.contact_data)

        self.assertEqual(Contact.objects.count(), 1)

        self.assertEqual(contact.first_name, 'Иван')
        self.assertEqual(contact.last_name, 'Петров')
        self.assertEqual(contact.phone_number, '+70000000000')
        self.assertEqual(contact.email, "test@test.tst")
        self.assertEqual(contact.user, self.user)

    def teststrfyUser(self):
        contact = Contact.objects.create(**self.contact_data)

        self.assertEqual(str(contact), "Иван Петров - +70000000000")
