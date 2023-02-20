import Core.models
import catalog.validators
import django.core.exceptions
import django.core.validators
import django.db.models


class Tag(Core.models.AbstractModel):
    id = django.db.models.AutoField(primary_key=True)
    slug = django.db.models.SlugField(
        help_text='max 200 символов',
        validators=[
            django.core.validators.MaxLengthValidator(200),
        ],
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Item(Core.models.AbstractModel):
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


class Category(Core.models.AbstractModel):
    slug = django.db.models.SlugField(
        help_text='max 200 символов',
        validators=[
            django.core.validators.MaxLengthValidator(200),
        ],
        unique=True,
    )
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

    def __str__(self):
        return self.name
