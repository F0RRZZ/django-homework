from django.test import Client, TestCase


class AboutPageTests(TestCase):
    def test_about_endpoint(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200,
                         'Error when going to the page "about"')
