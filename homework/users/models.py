import os

import django.contrib.auth.models
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import UserProfileManager


class UserProfile(
    django.contrib.auth.models.AbstractBaseUser,
    django.contrib.auth.models.PermissionsMixin,
):
    username = models.CharField(_('username'), max_length=150, unique=True)
    first_name = models.CharField(
        _('first name'), max_length=150, null=True, blank=True, help_text='Имя'
    )
    last_name = models.CharField(
        _('last name'),
        max_length=150,
        null=True,
        blank=True,
        help_text='Фамилия',
    )
    email = models.EmailField(
        _('email address'),
        null=True,
        blank=True,
        unique=True,
        help_text='Электронная почта',
    )
    date_joined = models.DateTimeField(
        _('date joined'), auto_now=True, help_text='Дата регистрации'
    )
    is_active = models.BooleanField(
        _('active'), default=False, help_text='Активен'
    )
    is_staff = models.BooleanField(
        _('staff'), default=False, help_text='Персонал'
    )
    is_superuser = models.BooleanField(
        _('superuser'), default=False, help_text='Суперпользователь'
    )
    birthday = models.DateTimeField(
        _('день рождения'), null=True, blank=True, help_text='День рождения'
    )
    image = models.ImageField(
        _('аватарка'),
        null=True,
        blank=True,
        help_text='Аватарка',
    )
    coffee_count = models.IntegerField(
        _('выпито кофе'), default=0, help_text='Кофе выпито'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserProfileManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def natural_key(self):
        return self.username

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

        if self.image:
            from django.core.files.storage import default_storage
            from django.core.files.base import ContentFile

            if not os.path.exists(f'avatars/{self.id}'):
                os.makedirs(f'avatars/{self.id}')

            filename = self.image.name
            path = f'avatars/{self.id}/{filename}'

            if default_storage.exists(path):
                default_storage.delete(path)
            default_storage.save(path, ContentFile(self.image.read()))
            self.image = path
            super(UserProfile, self).save(*args, **kwargs)
