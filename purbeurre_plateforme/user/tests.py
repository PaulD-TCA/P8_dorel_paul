from django.urls import reverse
from django.test import TestCase

from django.contrib.auth.models import User

# Create your tests here.
class RegisterPageTestCase(TestCase):
    def test_register_page(self):
        response = self.client.get(reverse('register_page'))
        self.assertEqual(response.status_code, 200)

    def test_user_creation(self):
        user_t = User.objects.create(password="password_test", username="Armelle", email="armelle@gmail.com")
        user_id = str(User.objects.get(password="password_test", username="Armelle", email="armelle@gmail.com").id)
        response = self.client.get(reverse('register_page'), args=(user_id,))
        self.assertEqual(response.status_code, 200)


class LoginPageTestCase(TestCase):
    def test_login_page(self):
        response = self.client.get(reverse('login_page'))
        self.assertEqual(response.status_code, 200)
