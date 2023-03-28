from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView

import catalog.models
import users.models


class UsersStat(ListView):
    template_name = 'statistic/users_stat.html'
    context_object_name = 'users'
    queryset = users.models.UserProfile.objects.get_statistic()


class ItemsStat(ListView):
    template_name = 'statistic/items_stat.html'
    context_object_name = 'items'
    queryset = catalog.models.Item.objects.get_statistic()


class UserItemsStat(ListView, LoginRequiredMixin):
    template_name = 'statistic/user_items_stat.html'
    context_object_name = 'items'

    def get_queryset(self):
        return catalog.models.Item.objects.get_user_statistic(self.request.user)
