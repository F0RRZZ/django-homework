import pytz

from django.utils import timezone

from users.models import UserProfile


def birthday_users(request):
    tz = pytz.timezone(request.session.get('django_timezone', 'UTC'))
    today = timezone.now().astimezone(tz).date()
    users = UserProfile.objects.filter(
        is_active=True, birthday__day=today.day, birthday__month=today.month
    )
    return {'birthday_users': users.values('first_name', 'last_name', 'email')}
