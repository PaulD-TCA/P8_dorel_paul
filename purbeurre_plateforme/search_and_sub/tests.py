from django.urls import reverse
from django.test import TestCase

from .models import Product, Backup
from django.contrib.auth.models import User


# Create your tests here.
class HomePageTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
#
class save_pageTestCase(TestCase):
    def test_save_page_returns_200(self):
        print("toto")
        produc_t = Product.objects.create(id=1, p_code=3274080005003, p_name="Eau Cristaline", p_nutrition_grade_fr="a", p_energy_kcal_100g=0, p_categories_tags="en:beverages,en:waters,en:spring-waters,en:mineral-waters,en:unsweetened-beverages", p_url="https://fr.openfoodfacts.org/produit/3274080005003", p_image_url="https://static.openfoodfacts.org/images/products/327/408/000/5003/front_fr.556.400.jpg")
        user_t = User.objects.create(id=100, password="password_test", username="Armelle", email="armelle@gmail.com")
        product_id_t = str(Product.objects.get(p_code=3274080005003, p_name="Eau Cristaline", p_nutrition_grade_fr="a", p_energy_kcal_100g=0, p_categories_tags="en:beverages,en:waters,en:spring-waters,en:mineral-waters,en:unsweetened-beverages", p_url="https://fr.openfoodfacts.org/produit/3274080005003", p_image_url="https://static.openfoodfacts.org/images/products/327/408/000/5003/front_fr.556.400.jpg").id)
        print(product_id_t)
        impossible = Backup.objects.create(id=1, b_date="2020-10-03 11:43:06.223159+02", p_id_id=1, u_id_id=100)
        backup_id = str(Backup.objects.get(p_id_id=1, u_id_id=100).id)
