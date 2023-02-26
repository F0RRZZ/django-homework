import catalog.models
import django.core.exceptions
from django.test import TestCase
from parameterized import parameterized


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
            is_published=True,
            name='Тестовый тег',
            slug='test-tag-slug',
        )

    def tearDown(self) -> None:
        super().tearDown()
        catalog.models.Item.objects.all().delete()
        catalog.models.Tag.objects.all().delete()
        catalog.models.Category.objects.all().delete()

    def test_create(self):
        item_count = catalog.models.Item.objects.count()
        self.item = catalog.models.Item(
            name='Тестовый товар',
            category=self.category,
            text='слово слово роскошно',
            main_image='1',
        )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(ModelsTests.tag)

        self.assertEqual(catalog.models.Item.objects.count(), item_count + 1)

    @parameterized.expand(
        [
            ('здесь тест не упадет(роскошно)',),
            ('роскошно, превосходно',),
            ('Роскошно!',),
            ('#ПрЕвоСХодно.,',),
        ]
    )
    def test_luxury_words_validator(self, case):
        try:
            self.item = catalog.models.Item(
                name=case,
                category=self.category,
                text=case,
                main_image='1',
            )
            self.item.full_clean()
            self.item.save()
        except django.core.exceptions.ValidationError:
            raise Exception(f'The test failed at the correct value: {case}')

    @parameterized.expand(
        [
            ('слово слово еще одно слово',),
            ('ыфдвлжыдвплжыдлвп',),
            ('здесь должен упасть тест',),
            ('роскошнопревосходно',),
            ('оченьроскошно',),
        ]
    )
    def test_luxury_words_negative_validator(self, case):
        with self.assertRaises(django.core.exceptions.ValidationError):
            self.item = catalog.models.Item(
                name=case,
                category=self.category,
                text=case,
            )
            self.item.full_clean()
            self.item.save()

    @parameterized.expand(
        [
            (
                'category',
                'slug-slug',
                300,
            ),
            (
                'категория',
                'slug___',
                20,
            ),
            (
                'categория',
                '_slug_',
                0,
            ),
            (
                'КатЕгория1',
                'SLUG',
                32767,
            ),
        ]
    )
    def test_category_validator(self, name, slug, weight):
        try:
            category = catalog.models.Category(
                name=name,
                slug=slug,
                weight=weight,
            )
            category.full_clean()
            category.save()
        except django.core.exceptions.ValidationError:
            raise Exception(
                f'The test failed at the correct values: name={name},'
                f' slug={slug}, weight: {weight}'
            )

    @parameterized.expand(
        [
            (
                'категория' * 150,
                'slug',
                777,
            ),
            (
                'категория',
                '#',
                666,
            ),
            ('category', 'sluuugg', 27365827658235),
        ]
    )
    def test_category_negative_validator(self, name, slug, weight):
        with self.assertRaises(django.core.exceptions.ValidationError):
            category = catalog.models.Category(
                name=name,
                slug=slug,
                weight=weight,
            )
            category.full_clean()
            category.save()

    def test_tags_name_repeat_validator(self):
        first_tag = catalog.models.Tag(
            is_published=True,
            name='тэг1',
            slug='test-tag-slug1',
        )
        first_tag.full_clean()
        first_tag.save()
        second_tag = catalog.models.Tag(
            is_published=True,
            name='тэг2',
            slug='test-tag-slug2',
        )
        second_tag.full_clean()
        second_tag.save()

    def test_negative_tags_name_repeat_validator(self):
        with self.assertRaises(django.core.exceptions.ValidationError):
            first_tag = catalog.models.Tag(
                is_published=True,
                name='тэг',
                slug='test-tag-slug1',
            )
            first_tag.full_clean()
            first_tag.save()
            second_tag = catalog.models.Tag(
                is_published=True,
                name='тэг',
                slug='test-tag-slug2',
            )
            second_tag.full_clean()
            second_tag.save()
