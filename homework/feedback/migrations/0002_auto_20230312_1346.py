# Generated by Django 3.2.16 on 2023-03-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.CharField(choices=[('received', 'получено'), ('processing', 'в обработке'), ('answered', 'ответ дан')], default='получено', max_length=20, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(help_text='введите почту, на которую будет отправлен ответ', max_length=254, verbose_name='почта'),
        ),
    ]
