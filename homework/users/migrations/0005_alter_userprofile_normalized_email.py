# Generated by Django 3.2.16 on 2023-03-23 19:46

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_failed_attempts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='normalized_email',
            field=users.models.NormalizedEmailField(blank=True, help_text='Нормализованная электронная почта', max_length=254, null=True, unique=True, verbose_name='нормализованная электронная почта'),
        ),
    ]