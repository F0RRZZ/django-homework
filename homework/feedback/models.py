import django.db.models


class Feedback(django.db.models.Model):
    text = django.db.models.TextField(
        'содержание письма',
        help_text='содержание письма',
    )
    created_on = django.db.models.DateTimeField(
        'время создания',
        auto_now_add=True,
        help_text='время создания письма',
    )
    email = django.db.models.EmailField(
        'почта',
        max_length=254,
        help_text='введите почту, на которую будет отправлен ответ',
    )
    status = django.db.models.CharField(
        'статус',
        max_length=20,
        choices=[
            ('received', 'получено'),
            ('processing', 'в обработке'),
            ('answered', 'ответ дан'),
        ],
        default='received',
    )
