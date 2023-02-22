import catalog.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.TextField(help_text='max 150 символов', validators=[django.core.validators.MaxLengthValidator(150)], verbose_name='Название')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(help_text='max 200 символов', unique=True, validators=[django.core.validators.MaxLengthValidator(200)])),
                ('weight', models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(32767)], verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.TextField(help_text='max 150 символов', validators=[django.core.validators.MaxLengthValidator(150)], verbose_name='Название')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(help_text='max 200 символов', unique=True, validators=[django.core.validators.MaxLengthValidator(200)])),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('name', models.TextField(help_text='max 150 символов', validators=[django.core.validators.MaxLengthValidator(150)], verbose_name='Название')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(help_text='Описание должно быть больше, чем из 2-х слов и содержать слова "превосходно" или "роскошно"', validators=[catalog.validators.luxury_words_validator], verbose_name='Описание')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='catalog_items', to='catalog.category', verbose_name='Категория')),
                ('tags', models.ManyToManyField(related_name='tags', to='catalog.Tag')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]