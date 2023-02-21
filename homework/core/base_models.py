import django.core.validators
import django.db.models


class PublishedWithNameBaseModel(django.db.models.Model):
    is_published = django.db.models.BooleanField('опубликовано', default=True)
    name = django.db.models.CharField(
        'название',
        help_text='Максимум 150 символов',
        max_length=150,
        unique=True,
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
