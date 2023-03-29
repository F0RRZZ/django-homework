from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

import catalog.models
import users.models
import rating.models


class UsersListView(ListView):
    template_name = 'statistic/users_stat.html'
    context_object_name = 'users'
    queryset = users.models.UserProfile.objects.filter(is_active=True)


class UsersStatisticsView(DetailView):
    template_name = 'statistic/user_stat_detail.html'

    def get(self, request, *args, **kwargs):
        username = users.models.UserProfile.objects.get_with_only_username(
            self.kwargs['pk'],
        ).username
        best_item = rating.models.Rating.objects.get_users_item(
            self.kwargs['pk'], 'max'
        )
        worst_item = rating.models.Rating.objects.get_users_item(
            self.kwargs['pk'], 'min'
        )
        ratings_stat = (
            rating.models.Rating.objects.get_users_ratings_count_and_avg(
                self.kwargs['pk']
            )
        )
        context = {
            'username': username,
            'best_item': best_item,
            'worst_item': worst_item,
            'ratings_count': ratings_stat.get('ratings_count'),
            'ratings_avg': ratings_stat.get('ratings_avg'),
        }
        return render(request, self.template_name, context)


class ItemsListView(ListView):
    template_name = 'statistic/items_stat.html'
    context_object_name = 'items'
    queryset = catalog.models.Item.objects.published()


class ItemsStatisticsView(DetailView):
    template_name = 'statistic/item_stat_detail.html'

    def get(self, request, *args, **kwargs):
        item_name = catalog.models.Item.objects.get_with_only_name(
            self.kwargs['pk']
        ).name
        item_stat = (
            rating.models.Rating.objects.get_items_ratings_count_and_avg(
                self.kwargs['pk']
            )
        )
        top_rater = rating.models.Rating.objects.get_item_rater(
            self.kwargs['pk'], 'max'
        )
        bottom_rater = rating.models.Rating.objects.get_item_rater(
            self.kwargs['pk'], 'min'
        )
        context = {
            'item_name': item_name,
            'ratings_count': item_stat.get('ratings_count'),
            'ratings_avg': item_stat.get('ratings_avg'),
            'top_rater': top_rater,
            'bottom_rater': bottom_rater,
        }
        return render(request, self.template_name, context)


class UserItemsStat(ListView, LoginRequiredMixin):
    template_name = 'statistic/user_items_stat.html'

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        items_list = rating.models.Rating.objects.get_users_items_list(user_id)
        context = {
            'ratings': items_list,
        }
        return render(request, self.template_name, context)
