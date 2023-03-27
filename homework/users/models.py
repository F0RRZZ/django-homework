import os
import re

import django.contrib.auth.models
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import UserProfileManager


class NormalizedEmailField(models.EmailField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if value:
            value = re.sub(r'(?i)(\<.*?\>)', '', value)

            if '@ya.ru' in value:
                value = value.split('@')[0] + '@yandex.ru'
            if '+' in value:
                value = (
                    f'{value.split("@")[0].split("+")[0]}@'
                    f'{value.split("@")[-1]}'
                )

            value = value.lower()

            if '@gmail.com' in value:
                username, domain = value.split('@')
                username = username.replace('.', '')
                value = f'{username}@{domain}'

            if '@yandex.ru' in value:
                username, domain = value.split('@')
                username = username.replace('.', '-')
                value = f'{username}@{domain}'

        return value


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
    normalized_email = NormalizedEmailField(
        _('нормализованная электронная почта'),
        null=True,
        blank=True,
        unique=True,
        help_text='Нормализованная электронная почта',
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

    def get_image_filename(self, filename):
        ext = os.path.splitext(filename)[-1]
        return 'avatars/user_{}{}'.format(self.id, ext)

    image = models.ImageField(
        _('аватарка'),
        upload_to=get_image_filename,
        null=True,
        blank=True,
        help_text='Аватарка',
    )
    coffee_count = models.IntegerField(
        _('выпито кофе'), default=0, help_text='Кофе выпито'
    )
    failed_attempts = models.IntegerField(
        _('неудачные попытки'), default=0, help_text='Неудачные попытки'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserProfileManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def natural_key(self):
        return self.username

    def save(self, *args, **kwargs):
        self.normalized_email = self.normalized_email or self.email
        super(UserProfile, self).save(*args, **kwargs)
