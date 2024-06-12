# tests.py
from django.test import TestCase
from django.urls import reverse
from core.models import UserModel
from django.conf import settings

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = UserModel.objects.create_user(username='testuser', password='password123', cpf='12345678901')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('password123'))
        self.assertEqual(user.cpf, '12345678901')

class ProductTest(TestCase):
    def test_add_product(self):
        response = self.client.post(reverse('add_product'), {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': '9.99',
            'image': ''
        })
        self.assertEqual(response.status_code, 200)
        product = settings.db.products.find_one({'name': 'Test Product'})
        self.assertIsNotNone(product)
        self.assertEqual(product['description'], 'Test Description')
        self.assertEqual(float(product['price']), 9.99)

    def test_list_products(self):
        settings.db.products.insert_one({'name': 'Test Product', 'description': 'Test Description', 'price': 9.99})
        response = self.client.get(reverse('list_products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
