from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

# from orders import views


class HomePageTests(SimpleTestCase):

    # check redirect index page
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 301)
        self.assertNotEqual(response.status_code, 404)

    # check orders page
    def test_home_page_status_code(self):
        response = self.client.get('/orders')
        # self.assertEquals(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
