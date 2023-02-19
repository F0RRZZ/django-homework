import django.core.validators
import django.db.models


class AbstractModel(django.db.models.Model):
    is_published = django.db.models.BooleanField('Опубликовано', default=True)
    name = django.db.models.TextField(
        'Название',
        help_text='max 150 символов',
        validators=[
            django.core.validators.MaxLengthValidator(150),
        ]
    )

    class Meta:
        abstract = True
