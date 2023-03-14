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
    personal_data = django.db.models.OneToOneField(
        'PersonalData',
        on_delete=django.db.models.CASCADE,
        blank=True,
        null=True,
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

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class FeedbackFile(django.db.models.Model):
    file = django.db.models.FileField(
        blank=True,
        null=True,
    )
    feedback = django.db.models.ForeignKey(
        Feedback,
        on_delete=django.db.models.CASCADE,
        related_name='feedback_files',
    )


class PersonalData(django.db.models.Model):
    email = django.db.models.EmailField(
        'почта',
        max_length=254,
        help_text='введите почту, на которую будет отправлен ответ',
    )
