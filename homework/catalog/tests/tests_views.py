from django.test import Client, TestCase
import django.urls

import catalog.models


class CatalogViewsTests(TestCase):
    def setUp(self) -> None:
        published_category = catalog.models.Category.objects.create(
            name='published_category',
            slug='published_category',
        )
        unpublished_category = catalog.models.Category.objects.create(
            name='unpublished_category',
            slug='unpublished_category',
            is_published=False,
        )
        published_tag = catalog.models.Tag.objects.create(
            name='published_tag',
            slug='published_tag',
        )
        unpublished_tag = catalog.models.Tag.objects.create(
            name='unpublished_tag',
            slug='unpublished_tag',
            is_published=False,
        )
        published_item_on_main = catalog.models.Item.objects.create(
            name='published_item_on_main',
            text='роскошно',
            category=published_category,
            is_on_main=True,
        )
        published_item_not_on_main = catalog.models.Item.objects.create(
            name='published_item_not_on_main',
            text='роскошно',
            category=published_category,
        )
        unpublished_item = catalog.models.Item.objects.create(
            name='unpublished_item',
            text='роскошно',
            category=unpublished_category,
        )

        published_category.save()
        unpublished_category.save()

        published_tag.save()
        unpublished_tag.save()

        published_item_on_main.clean()
        published_item_on_main.save()
        published_item_not_on_main.clean()
        published_item_not_on_main.save()
        unpublished_item.clean()
        unpublished_item.save()

    def test_home_page_show_correct_context(self):
        response = Client().get(django.urls.reverse('homepage:index'))
        self.assertIn('items', response.context)

    def test_home_count_item(self):
        response = Client().get(django.urls.reverse('homepage:index'))
        items = response.context['items']
        self.assertEqual(items.count(), 1)

    def test_catalog_show_correct_context(self):
        response = Client().get('/catalog/')
        self.assertIn('items', response.context)

    def test_catalog_count_item(self):
        response = Client().get('/catalog/')
        items = response.context['items']
        self.assertEqual(items.count(), 2)
