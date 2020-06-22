from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_add_song_to_repertoire(self):
        # Peter has heard of a new app to manage a repertoire of songs
        self.browser.get(self.live_server_url)
        # He sees he found the right place by looking at the page header
        self.assertIn('SongsICanPlay', self.browser.title)

        self.fail('finish test!')
