from django.test import TestCase
from django.urls import reverse
from .models import User

class UserRegistrationTests(TestCase):

    def test_register_page_status_code(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_page_template(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'core/register.html')

    def test_register_form(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())
