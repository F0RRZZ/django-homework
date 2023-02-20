import catalog.validators
import Core.models
import django.core.exceptions
import django.core.validators
import django.db.models


class Tag(
    Core.models.PublishedWithNameBaseModel,
    Core.models.SluggedBaseModel,
):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Item(Core.models.PublishedWithNameBaseModel):
    category = django.db.models.ForeignKey(
        'category',
        on_delete=django.db.models.CASCADE,
        verbose_name='категория',
        related_name='catalog_items',
    )
    tags = django.db.models.ManyToManyField(Tag, related_name='tags')
    text = django.db.models.TextField(
        'описание',
        help_text=(
            'Описание должно содержать слова "превосходно" или "роскошно"'
        ),
        validators=[
            catalog.validators.luxury_words_validator,
        ],
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.text[:15]


class Category(
    Core.models.PublishedWithNameBaseModel,
    Core.models.SluggedBaseModel,
):
    weight = django.db.models.IntegerField(
        'вес',
        default=100,
        validators=[
            django.core.validators.MinValueValidator(0),
            django.core.validators.MaxValueValidator(32767),
        ],
        help_text=(
            'Укажите вес. Минимальное значение - 0, максимальное - 32767'
        ),
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
