from http import HTTPStatus

from django.test import Client, TestCase


class CatalogPageTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            'Error when going to the page "catalog"',
        )

    def test_catalog_item_endpoint(self):
        response = Client().get('/catalog/1/')
        response_str = Client().get('/catalog/item/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            'Error with the right type of item (/catalog/1/)',
        )

        self.assertEqual(
            response_str.status_code,
            HTTPStatus.NOT_FOUND,
            'Item url with string worked (/catalog/item/)',
        )

    def test_catalog_item_positive_integer_endpoint(self):
        urls = ['/catalog/re/{}/', '/catalog/converter/{}']
        cases = [
            ('1', HTTPStatus.OK),
            ('10', HTTPStatus.OK),
            ('235236236', HTTPStatus.OK),
            ('0', HTTPStatus.NOT_FOUND),
            ('-1', HTTPStatus.NOT_FOUND),
            ('010', HTTPStatus.NOT_FOUND),
            ('1.0', HTTPStatus.NOT_FOUND),
            ('1a', HTTPStatus.NOT_FOUND),
            ('a', HTTPStatus.NOT_FOUND),
            ('^1', HTTPStatus.NOT_FOUND),
            ('aa1', HTTPStatus.NOT_FOUND),
            ('z1x', HTTPStatus.NOT_FOUND),
            ('^1.0', HTTPStatus.NOT_FOUND),
        ]
        for url in urls:
            for case in cases:
                test_url = url.format(case[0])
                response = Client().get(test_url)
                self.assertEqual(
                    response.status_code, case[1], f'(URL: {test_url})'
                )
