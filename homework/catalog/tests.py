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
            response.status_code, 404, 'Clicking on an incorrect product link'
        )