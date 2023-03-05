import ckeditor.fields
import django.core.exceptions
import django.core.validators
import django.db.models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

import catalog.managers
import catalog.validators
import core.base_models


class Category(
    core.base_models.PublishedWithNameBaseModel,
    core.base_models.SluggedBaseModel,
    core.base_models.SaveAndCleanModifiedBaseMethod,
):
    formatted_name = django.db.models.CharField(
        'форматированное имя',
        max_length=150,
        null=True,
        editable=False,
    )
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


class GalleryImage(django.db.models.Model):
    item = django.db.models.ForeignKey(
        'Item',
        on_delete=django.db.models.CASCADE,
    )

    image = django.db.models.ImageField(
        'Галерея',
        upload_to='catalog/',
        null=True,
    )

    class Meta:
        verbose_name = 'дополнительное фото'
        verbose_name_plural = 'дополнительные фото'

    def get_image(self):
        return get_thumbnail(
            self.image,
            '300x300',
            crop='center',
            quality=51,
        )


class Item(core.base_models.PublishedWithNameBaseModel):
    objects = catalog.managers.ItemManager()

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

    text = ckeditor.fields.RichTextField(
        verbose_name='описание',
        blank=True,
        null=True,
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
    is_on_main = django.db.models.BooleanField(
        'на главной',
        default=False,
    )

    class Meta:
        default_related_name = 'items'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.text[:15]


class MainImage(django.db.models.Model):
    item = django.db.models.OneToOneField(
        Item,
        on_delete=django.db.models.CASCADE,
        null=True,
    )

    image = django.db.models.ImageField(
        'Главное изображение',
        upload_to='catalog/',
        null=True,
    )

    def get_image(self):
        return get_thumbnail(
            self.image,
            '300x300',
            crop='center',
            quality=51,
        )

    def image_thumbnail(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50">')
        return 'Нет изображения'

    image_thumbnail.short_description = 'превью'
    image_thumbnail.allow_tags = True

    class Meta:
        default_related_name = 'main_image'
        verbose_name = 'главное изображение'


class Tag(
    core.base_models.PublishedWithNameBaseModel,
    core.base_models.SluggedBaseModel,
    core.base_models.SaveAndCleanModifiedBaseMethod,
):
    formatted_name = django.db.models.CharField(
        'форматированное имя',
        max_length=150,
        null=True,
        editable=False,
    )

    class Meta:
        default_related_name = 'tags'
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
