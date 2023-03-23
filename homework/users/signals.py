from django.conf import settings
from django.contrib.auth.signals import user_login_failed, user_logged_in
from django.core.mail import send_mail
from django.dispatch import receiver

from users.models import UserProfile


@receiver(user_login_failed)
def handle_login_failed(sender, credentials, **kwargs):
    username = credentials.get('username')
    try:
        user = UserProfile.objects.get(username=username)
    except UserProfile.DoesNotExist:
        return 'User not founded'
    user.failed_attempts = user.failed_attempts + 1
    if user.failed_attempts == settings.MAX_FAILED_ATTEMPTS and user.is_active:
        user.is_active = False
        user.failed_attempts = 0
        send_mail(
            'Активация аккаунта',
            f'Ваш аккаунт был заблокирован из-за слишком многих неудачных'
            f' попыток входа. Чтобы разблокировать свой аккаунт,'
            f' перейдите по ссылке:'
            f' http://127.0.0.1:8000/auth/activate/{user.username}/',
            settings.EMAIL,
            [user.email],
            fail_silently=False,
        )
        print(user.email)
    user.save()


@receiver(user_logged_in)
def handle_login_done(sender, user, **kwargs):
    username = user.username
    print(username)
    try:
        user_profile = UserProfile.objects.get(username=username)
    except UserProfile.DoesNotExist:
        return 'User not found'
    user_profile.failed_attempts = 0
    user_profile.save()
