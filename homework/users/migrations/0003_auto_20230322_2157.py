# Generated by Django 3.2.16 on 2023-03-22 18:57

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230322_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='normalized_email',
            field=users.models.NormalizedEmailField(blank=True, help_text='Нормализованная электронная почта', max_length=254, null=True, unique=True, verbose_name='normalized email address'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateTimeField(blank=True, help_text='День рождения', null=True, verbose_name='день рождения'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='coffee_count',
            field=models.IntegerField(default=0, help_text='Кофе выпито', verbose_name='выпито кофе'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(auto_now=True, help_text='Дата регистрации', verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, help_text='Электронная почта', max_length=254, null=True, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, help_text='Имя', max_length=150, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, help_text='Аватарка', null=True, upload_to='', verbose_name='аватарка'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Активен', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Персонал', verbose_name='staff'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Суперпользователь', verbose_name='superuser'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, help_text='Фамилия', max_length=150, null=True, verbose_name='last name'),
        ),
    ]
