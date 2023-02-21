import catalog.models
import django.core.exceptions
from django.test import TestCase


class ModelsTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.category = catalog.models.Category.objects.create(
            is_published=True,
            name='Тестовая категория',
            slug='test-category-slug',
            weight=100,
        )
        cls.tag = catalog.models.Tag.objects.create(
            is_published=True, name='Тестовый тег', slug='test-tag-slug'
        )

    def test_unable_create_one_letter(self):
        item_count = catalog.models.Item.objects.count()
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                name='Тестовый товар', category=self.category, text='1'
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(ModelsTests.tag)

        self.assertEqual(catalog.models.Item.objects.count(), item_count)

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

        self.assertEqual(catalog.models.Item.objects.count(), item_count + 1)

    def test_luxury_words_validator(self):
        cases = [
            ('слово слово еще одно слово', False),
            ('ыфдвлжыдвплжыдлвп слово word', False),
            ('здесь должен упасть тест', False),
            ('здесь тест не упадет(роскошно)', True),
            ('роскошно, превосходно слово', True),
            ('роскошнопревосходно слово слово', True),
            ('оченьроскошно слово слово', True),
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
