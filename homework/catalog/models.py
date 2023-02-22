import catalog.validators
import core.base_models
import string
import django.core.exceptions
import django.core.validators
import django.db.models


class Category(
    core.base_models.PublishedWithNameBaseModel,
    core.base_models.SluggedBaseModel,
):
    weight = django.db.models.PositiveSmallIntegerField(
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
        default_related_name = 'categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def clean(self):
        formatted_name = self.name.lower()
        for symbol in string.punctuation:
            formatted_name = formatted_name.replace(symbol, '')
        if self.__class__.objects.filter(name=formatted_name).exists():
            raise django.core.validators.ValidationError(
                'Название категории должно быть уникальным.'
            )
        return self.name


class Item(core.base_models.PublishedWithNameBaseModel):
    category = django.db.models.ForeignKey(
        Category,
        on_delete=django.db.models.CASCADE,
        verbose_name='категория',
        related_name='items',
        related_query_name='item',
        null=True,
    )
    tags = django.db.models.ManyToManyField(
        'tag',
        related_name='tags',
        related_query_name='tag',
    )
    text = django.db.models.TextField(
        'описание',
        help_text=(
            'Описание должно содержать слова "превосходно" или "роскошно"'
        ),
        validators=[
            catalog.validators.ValidateMustContain(
                'роскошно',
                'превосходно',
            ),
        ],
    )

    class Meta:
        default_related_name = 'items'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.text[:15]


class Tag(
    core.base_models.PublishedWithNameBaseModel,
    core.base_models.SluggedBaseModel,
):
    class Meta:
        default_related_name = 'tags'
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def clean(self):
        formatted_name = self.name.lower()
        for symbol in string.punctuation:
            formatted_name = formatted_name.replace(symbol, '')
        if self.__class__.objects.filter(name=formatted_name).exists():
            raise django.core.validators.ValidationError(
                'Название должно быть уникальным.'
            )
        return self.name
