from selenium import webdriver
# from search_and_sub.models import Product, Backup
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from selenium.webdriver.common.keys import Keys
from django.contrib.auth import get_user_model
from django.test import Client
# driver = webdriver.Chrome(executable_path="../test_nav_web/chromedriver.exe")

class TestProject(StaticLiveServerTestCase):

    def setUp(self):
        self.User = get_user_model()
        self.browser = webdriver.Chrome('../functional_tests/chromedriver1')
        self.home_url = self.live_server_url + reverse('home')
        self.result_url = self.live_server_url + reverse('result')
        self.registrer_url = self.live_server_url + reverse('registration')
        self.login_url = self.live_server_url + reverse('login')
        self.account_url = self.live_server_url + reverse('account')
        self.food_url = self.live_server_url + reverse('myfood')
        self.client = Client()



    # def test_registrer(self):
    #     self.registrer()
    #     self.assertEquals(
    #         self.browser.current_url,
    #         self.index_url
    #     )
    #     self.browser.close()

    # def test_open_project(self):
    #     self.browser.get(self.live_server_url)
    #     self.browser.close()
    def tearDown(self):
        self.browser.close()

    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        time.sleep(1)
