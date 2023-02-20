import catalog.validators
import Core.models
import django.core.exceptions
import django.core.validators
import django.db.models


class Tag(
    Core.models.PublishedWithNameBaseModel, Core.models.SluggedBaseModel,
):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Item(Core.models.PublishedWithNameBaseModel):
    category = django.db.models.ForeignKey(
        'category',
        on_delete=django.db.models.CASCADE,
        verbose_name='Категория',
        related_name='catalog_items',
    )
    tags = django.db.models.ManyToManyField(Tag, related_name='tags')
    text = django.db.models.TextField(
        'Описание',
        help_text='Описание должно быть больше, чем из 2-х слов и содержать '
        'слова "превосходно" или "роскошно"',
        validators=[
            catalog.validators.luxury_words_validator,
            catalog.validators.words_count_validator,
        ],
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.text[:15]


class Category(
    Core.models.PublishedWithNameBaseModel, Core.models.SluggedBaseModel,
):
    weight = django.db.models.IntegerField(
        'Вес',
        default=100,
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(32767),
        ],
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
