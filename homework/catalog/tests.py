import catalog.models
import django.core.exceptions
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


class ModelsTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.category = catalog.models.Category.objects.create(
            is_published=True,
            name='Тестовая категория',
            slug='test-category-slug',
            weight=100
        )
        cls.tag = catalog.models.Tag.objects.create(
            is_published=True,
            name='Тестовый тег',
            slug='test-tag-slug'
        )

    def test_unable_create_one_letter(self):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                name='Тестовый товар',
                category=self.category,
                text='1'
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTests.tag)

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count
        )

    def test_create(self):
        item_count = catalog.models.Item.objects.count()
        self.item = catalog.models.Item(
            name='Тестовый товар',
            category=self.category,
            text='слово слово роскошно',
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(ModelsTests.tag)

        self.assertEqual(
            catalog.models.Item.objects.count(),
            item_count + 1
        )

    def test_luxury_words_validator(self):
        cases = [
            ('слово слово еще одно слово', False),
            ('ыфдвлжыдвплжыдлвп слово word', False),
            ('здесь должен упасть тест', False),
            ('здесь тест не упадет(роскошно)', True),
            ('роскошно, превосходно слово', True),
            ('роскошнопревосходно слово слово', True),
            ('оченьроскошно слово слово', True)
        ]
        for case, result in cases:
            failed = False
            try:
                self.item = catalog.models.Item(
                    name='Тестовый товар',
                    category=self.category,
                    text=case,
                )
                self.item.full_clean()
                self.item.save()
            except django.core.exceptions.ValidationError:
                if result:
                    raise Exception(
                        f'The test failed at the correct value: {case}'
                    )
                failed = True
            if not failed and not result:
                raise Exception(
                    f'The tests not failed at the incorrect value: {case}'
                )

    def test_words_count_validator(self):
        cases = [
            ('роскошно превосходно', False),
            ('роскошно превосходно слово', True),
            ('роскошно слово ', False)
        ]
        for case, result in cases:
            failed = False
            try:
                self.item = catalog.models.Item(
                    name='Тестовый товар',
                    category=self.category,
                    text=case,
                )
                self.item.full_clean()
                self.item.save()
            except django.core.exceptions.ValidationError:
                if result:
                    raise Exception(
                        f'The test failed at the correct value: {case}'
                    )
                failed = True
            if not failed and not result:
                raise Exception(
                    f'The tests not failed at the incorrect value: {case}'
                )
