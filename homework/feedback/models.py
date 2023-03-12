import django.db.models
from django.utils import timezone


class Feedback(django.db.models.Model):
    text = django.db.models.TextField(
        'содержание письма',
        help_text='содержание письма',
    )
    created_on = django.db.models.DateTimeField(
        'время создания',
        default=timezone.now,
        help_text='время создания письма',
    )
    email = django.db.models.EmailField(
        'почта',
        help_text='введите почту, на которую будет отправлен ответ',
    )
