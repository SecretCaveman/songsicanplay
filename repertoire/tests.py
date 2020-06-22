from django.test import TestCase
from django.urls import resolve
from repertoire.views import home_page

class HomePageTest(TestCase):

    def test_root_url_redirects_to_home(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)