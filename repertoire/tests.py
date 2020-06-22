from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from repertoire.views import home_page

class HomePageTest(TestCase):

    def test_root_url_redirects_to_home(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed('home.html')