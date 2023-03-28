from django.conf import settings
from django.db import models

from catalog.models import Item
from rating.managers import RatingManager


class Rating(models.Model):
    RATING_CHOICES = [
        (1, 'Ненависть'),
        (2, 'Неприязнь'),
        (3, 'Нейтрально'),
        (4, 'Обожание'),
        (5, 'Любовь'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='товар',
        related_name='ratings',
    )
    rating = models.PositiveSmallIntegerField(
        'моя оценка',
        choices=RATING_CHOICES,
        null=True,
        blank=True,
    )

    objects = RatingManager()

    class Meta:
        verbose_name = 'оценка'
        verbose_name_plural = 'оценки'
        unique_together = ('user', 'item')
