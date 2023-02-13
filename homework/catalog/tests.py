from http import HTTPStatus

from django.test import Client, TestCase


class CatalogPageTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            'Error when going to the page "catalog"'
        )

    def test_item_choice(self):
        response = Client().get('/catalog/1/')
        response_str = Client().get('/catalog/item/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            'Error with the right type of item'
        )

        self.assertEqual(
            response_str.status_code,
            HTTPStatus.NOT_FOUND,
            'Item link with string worked'
        )

    def test_link_with_regex(self):
        response = Client().get('/catalog/re/1/')
        response_negative_number = Client().get('/catalog/re/-1/')
        response_str = Client().get('/catalog/re/a/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            'Error with the right regex'
        )

        self.assertEqual(
            response_negative_number.status_code,
            HTTPStatus.NOT_FOUND,
            'Regex with negative number worked',
        )

        self.assertEqual(
            response_str.status_code,
            HTTPStatus.NOT_FOUND,
            'Regex with string worked'
        )

    def test_link_with_positive_number(self):
        response = Client().get('/catalog/converter/1')
        response_negative_number = Client().get('/catalog/converter/-1')
        response_str = Client().get('/catalog/converter/a')
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            'Error with the positive number'
        )

        self.assertEqual(
            response_negative_number.status_code,
            HTTPStatus.NOT_FOUND,
            'Link with negative number worked',
        )

        self.assertEqual(
            response_str.status_code,
            HTTPStatus.NOT_FOUND,
            'Link with string worked'
        )
