from django.contrib.auth.backends import ModelBackend, UserModel

from users.models import UserProfile


class NormalizedEmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserProfile.objects.get(normalized_email=username)
        except UserProfile.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(
                user
            ):
                return user
