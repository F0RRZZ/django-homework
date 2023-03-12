# Generated by Django 3.2.16 on 2023-03-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20230308_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='время создания', verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_on_main',
            field=models.BooleanField(default=False, help_text='отображение товара на главной странице', verbose_name='на главной'),
        ),
        migrations.AlterField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='последнее изменение', verbose_name='последнее изменение'),
        ),
    ]
