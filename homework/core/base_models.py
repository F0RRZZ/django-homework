import django.core.validators
import django.db.models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

import core.tools


class PublishedWithNameBaseModel(django.db.models.Model):
    is_published = django.db.models.BooleanField(
        'опубликовано',
        default=True,
    )
    name = django.db.models.CharField(
        'название',
        help_text='Максимум 150 символов',
        max_length=150,
        null=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class SluggedBaseModel(django.db.models.Model):
    slug = django.db.models.SlugField(
        help_text='Максимум 200 символов',
        validators=[
            django.core.validators.MaxLengthValidator(200),
        ],
        unique=True,
    )

    class Meta:
        abstract = True


class SaveAndCleanModifiedBaseMethod(django.db.models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.formatted_name = core.tools.name_formatter(self.name)
        super().save(*args, **kwargs)

    def clean(self):
        formatted_name = core.tools.name_formatter(self.name)
        if self.__class__.objects.filter(
            formatted_name=formatted_name
        ).exists():
            raise django.core.validators.ValidationError(
                'Название должно быть уникальным.'
            )
        return self.name


class ImageBaseModel(django.db.models.Model):
    image = django.db.models.ImageField(
        'Будет приведено к ширине 300x300',
        upload_to='catalog/',
        null=True,
    )

    class Meta:
        abstract = True

    def get_image(self):
        return get_thumbnail(
            self.image,
            '300x300',
            crop='center',
            quality=51,
        )

    def image_thumbnail(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" width="50">'
            )
        return 'Нет изображения'

    image_thumbnail.short_description = 'превью'
    image.allow_tags = True
