# Generated by Django 3.2.16 on 2023-03-29 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_alter_galleryimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='rating',
        ),
    ]