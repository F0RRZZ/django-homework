from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    birthday = models.DateTimeField(
        'дата рождения',
        null=True,
        blank=True,
    )
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    coffee_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Дополнительное поле'
        verbose_name_plural = 'Дополнительные поля'
