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

    def test_item_choice(self):
        response = Client().get('/catalog/1/')
        response_str = Client().get('/catalog/item/')
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            'Error with the right type of item',
        )

        self.assertEqual(
            response_str.status_code,
            HTTPStatus.NOT_FOUND,
            'Item link with string worked',
        )

    def test_link_with_regex(self):
        cases = [
            ('/catalog/re/1/', HTTPStatus.OK),
            ('/catalog/re/10/', HTTPStatus.OK),
            ('/catalog/re/235236236/', HTTPStatus.OK),
            ('/catalog/re/0/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/-1/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/010/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/1.0/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/1a/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/a/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/^1/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/aa1/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/z1x/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/^1.0/', HTTPStatus.NOT_FOUND),
        ]
        for case in cases:
            response = Client().get(case[0])
            self.assertEqual(
                response.status_code,
                case[1],
            )

    def test_link_with_positive_number(self):
        cases = [
            ('/catalog/re/1/', HTTPStatus.OK),
            ('/catalog/re/10/', HTTPStatus.OK),
            ('/catalog/re/235236236/', HTTPStatus.OK),
            ('/catalog/re/0/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/-1/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/010/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/1.0/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/1a/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/a/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/^1/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/aa1/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/z1x/', HTTPStatus.NOT_FOUND),
            ('/catalog/re/^1.0/', HTTPStatus.NOT_FOUND),
        ]
        for case in cases:
            response = Client().get(case[0])
            self.assertEqual(
                response.status_code,
                case[1],
            )
