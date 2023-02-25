import string

import django.core.validators
import django.db.models


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
        formatted_name = self.name.lower()
        for symbol in string.punctuation:
            formatted_name = formatted_name.replace(symbol, '')
        self.formatted_name = formatted_name.replace(' ', '')
        super().save(*args, **kwargs)

    def clean(self):
        formatted_name = self.name.lower()
        for symbol in string.punctuation:
            formatted_name = formatted_name.replace(symbol, '')
        formatted_name = formatted_name.replace(' ', '')
        if self.__class__.objects.filter(
            formatted_name=formatted_name
        ).exists():
            raise django.core.validators.ValidationError(
                'Название должно быть уникальным.'
            )
        return self.name

