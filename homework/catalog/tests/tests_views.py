from django.test import Client, TestCase
import django.urls


class CatalogViewsTests(TestCase):
    fixtures = ['data.json']

    def test_home_page_show_correct_context(self):
        response = Client().get(django.urls.reverse('homepage:index'))
        self.assertIn('items', response.context)
        self.assertNotIn('categories', response.context)

    def test_home_count_item(self):
        response = Client().get(django.urls.reverse('homepage:index'))
        items = response.context['items']
        self.assertEqual(len(items), 2)

    def test_catalog_show_correct_context(self):
        response = Client().get('/catalog/')
        self.assertIn('categories', response.context)
        self.assertNotIn('items', response.context)

    def test_catalog_count_categories(self):
        response = Client().get('/catalog/')
        categories = response.context['categories']
        self.assertEqual(len(categories), 2)
