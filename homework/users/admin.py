from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import UserProfile


class ProfileInlined(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInlined,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
