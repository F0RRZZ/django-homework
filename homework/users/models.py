import django.contrib.auth.models
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfileManager(django.contrib.auth.models.BaseUserManager):
    def get_by_natural_key(self, value):
        if '@' in value:
            return self.get(email__iexact=value)
        return self.get(username__iexact=value)

    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        if email and self.filter(email__iexact=email).exists():
            raise ValueError('User with this email already exists')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(username, email, password, **extra_fields)


class UserProfile(
    django.contrib.auth.models.AbstractBaseUser,
    django.contrib.auth.models.PermissionsMixin,
):
    username = models.CharField(_('username'), max_length=150, unique=True)
    first_name = models.CharField(
        _('first name'), max_length=150, null=True, blank=True
    )
    last_name = models.CharField(
        _('last name'), max_length=150, null=True, blank=True
    )
    email = models.EmailField(
        _('email address'), null=True, blank=True, unique=True
    )
    date_joined = models.DateTimeField(_('date joined'), auto_now=True)
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    birthday = models.DateTimeField(_('день рождения'), null=True, blank=True)
    image = models.ImageField(_('аватарка'), null=True, blank=True)
    coffee_count = models.IntegerField(_('выпито кофе'), default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserProfileManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def natural_key(self):
        return self.username
