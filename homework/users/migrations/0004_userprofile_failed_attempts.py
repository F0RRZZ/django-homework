# Generated by Django 3.2.16 on 2023-03-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230322_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='failed_attempts',
            field=models.IntegerField(default=0, help_text='Неудачные попытки', verbose_name='неудачные попытки'),
        ),
    ]
