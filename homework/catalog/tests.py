from django.test import Client, TestCase


class CatalogPageTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(
            response.status_code, 200, 'Error when going to the page "catalog"'
        )

    def test_right_item_choice(self):
        response = Client().get('/catalog/1/')
        self.assertEqual(
            response.status_code, 200, 'Error with the right type of item'
        )

    def test_wrong_item_choice(self):
        response = Client().get('/catalog/item/')
        self.assertEqual(
            response.status_code, 404, 'Invalid product link worked'
        )

    def test_right_link_with_regex(self):
        response = Client().get('/catalog/re/1/')
        self.assertEqual(
            response.status_code, 200, 'Error with the right regex'
        )

    def test_wrong_link_with_regex(self):
        response_negative_number = Client().get('/catalog/re/-1/')
        self.assertEqual(
            response_negative_number.status_code,
            404,
            'Regex with negative number worked'
        )

        response_str = Client().get('/catalog/re/a/')
        self.assertEqual(
            response_str.status_code, 404, 'Regex with string worked'
        )

    def test_right_link_with_positive_number(self):
        response = Client().get('/catalog/converter/1')
        self.assertEqual(
            response.status_code, 200, 'Error with the positive number'
        )

    def test_wrong_link_with_positive_number(self):
        response_negative_number = Client().get('/catalog/converter/-1')
        self.assertEqual(
            response_negative_number.status_code,
            404,
            'Link with negative number worked'
        )

        response_str = Client().get('/catalog/converter/a')
        self.assertEqual(
            response_str.status_code, 404, 'Link with string worked'
        )
