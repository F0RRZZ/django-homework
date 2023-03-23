from django.conf import settings
from django.contrib.auth.signals import user_login_failed
from django.core.mail import send_mail
from django.dispatch import receiver

from users.models import UserProfile


@receiver(user_login_failed)
def handle_login_failed(sender, credentials, **kwargs):
    username = credentials.get('username')
    try:
        user = UserProfile.objects.get(username=username)
    except UserProfile.DoesNotExist:
        return
    user.failed_attempts = user.failed_attempts + 1
    if user.failed_attempts == settings.MAX_FAILED_ATTEMPTS:
        user.is_active = False
        user.failed_attempts = 0
        send_mail(
            'Активация аккаунта',
            f'Ссылка для активации:'
            f' http://127.0.0.1:8000/auth/activate/{user.username}/',
            settings.EMAIL,
            [user.email],
            fail_silently=False,
        )
    user.save()
