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
            'здесь тест не упадет(роскошно)',
            'роскошно, превосходно',
            'Роскошно!',
            '#ПрЕвоСХодно.,'
        ]
        for case in cases:
            try:
                self.item = catalog.models.Item(
                    name=case,
                    category=self.category,
                    text=case,
                )
                self.item.full_clean()
                self.item.save()
            except django.core.exceptions.ValidationError:
                raise Exception(
                    f'The test failed at the correct value: {case}'
                )

    def test_luxury_words_negative_validator(self):
        cases = [
            'слово слово еще одно слово',
            'ыфдвлжыдвплжыдлвп',
            'здесь должен упасть тест',
            'роскошнопревосходно',
            'оченьроскошно',
        ]
        for case in cases:
            with self.assertRaises(django.core.exceptions.ValidationError):
                self.item = catalog.models.Item(
                    name=case,
                    category=self.category,
                    text=case,
                )
                self.item.full_clean()
                self.item.save()
