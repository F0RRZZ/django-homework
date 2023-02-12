from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200,
                         'Error when going to the homepage')
