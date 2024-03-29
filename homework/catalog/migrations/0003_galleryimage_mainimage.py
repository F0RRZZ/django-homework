# Generated by Django 3.2.16 on 2023-02-26 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20230223_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='catalog/', verbose_name='Будет приведено к ширине 300x300')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.item')),
            ],
            options={
                'verbose_name': 'главное фото',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='catalog/', verbose_name='Будет приведено к ширине 300x300')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.item')),
            ],
            options={
                'verbose_name': 'дополнительное фото',
                'verbose_name_plural': 'дополнительные фото',
            },
        ),
    ]
