from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        response = Client().get('/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            'Error when going to the homepage',
        )

    def test_coffee_endpoint_status(self):
        response = Client().get('/coffee/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.IM_A_TEAPOT,
            'Endpoint /coffee does not return 418 status code',
        )

    def test_coffee_endpoint_text(self):
        ...
