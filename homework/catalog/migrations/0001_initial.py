# Generated by Django 3.2.16 on 2023-02-22 10:39

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('name', models.CharField(help_text='Максимум 150 символов', max_length=150, unique=True, verbose_name='название')),
                ('slug', models.SlugField(help_text='Максимум 200 символов', unique=True, validators=[django.core.validators.MaxLengthValidator(200)])),
                ('weight', models.PositiveSmallIntegerField(default=100, help_text='Укажите вес. Минимальное значение - 0, максимальное - 32767', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(32767)], verbose_name='вес')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('name', models.CharField(help_text='Максимум 150 символов', max_length=150, unique=True, verbose_name='название')),
                ('slug', models.SlugField(help_text='Максимум 200 символов', unique=True, validators=[django.core.validators.MaxLengthValidator(200)])),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('name', models.CharField(help_text='Максимум 150 символов', max_length=150, unique=True, verbose_name='название')),
                ('text', models.TextField(help_text='Описание должно содержать слова "превосходно" или "роскошно"', validators=[catalog.validators.ValidateMustContain('роскошно', 'превосходно')], verbose_name='описание')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', related_query_name='item', to='catalog.category', verbose_name='категория')),
                ('tags', models.ManyToManyField(related_name='tags', related_query_name='tag', to='catalog.Tag')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
    ]
