import django.core.validators
import django.db.models


class PublishedWithNameBaseModel(django.db.models.Model):
    is_published = django.db.models.BooleanField('Опубликовано', default=True)
    name = django.db.models.TextField(
        'Название',
        help_text='max 150 символов',
        validators=[
            django.core.validators.MaxLengthValidator(150),
        ],
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class SluggedBaseModel(django.db.models.Model):
    slug = django.db.models.SlugField(
        help_text='max 200 символов',
        validators=[
            django.core.validators.MaxLengthValidator(200),
        ],
        unique=True,
    )

    class Meta:
        abstract = True
