import django.core.validators
from django.forms import ValidationError


class NotEmptyString(django.core.validators.BaseValidator):
    def __call__(self, value):
        if not value.replace(' ', ''):
            raise ValidationError('Текст не может быть пустым')
