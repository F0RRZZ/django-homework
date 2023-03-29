from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

import catalog.models
import users.models
import rating.models


class UsersListView(ListView):
    template_name = 'statistic/users_stat.html'
    context_object_name = 'users'
    queryset = users.models.UserProfile.objects.all()


class UsersStatisticsView(DetailView):
    template_name = 'statistic/users_stat.html'

    def get(self, request, *args, **kwargs):
        best_item = rating.models.Rating.objects.get_users_best_item(
            self.kwargs['pk']
        )
        worst_item = rating.models.Rating.objects.get_users_worst_item(
            self.kwargs['pk']
        )
        ratings_count = rating.models.Rating.objects.get_users_ratings_count(
            self.kwargs['pk']
        )
        ratings_avg = rating.models.Rating.objects.get_users_ratings_avg(
            self.kwargs['pk']
        )
        context = {
            'best_item': best_item,
            'worst_item': worst_item,
            'ratings_count': ratings_count.get('ratings_count'),
            'ratings_avg': ratings_avg.get('ratings_avg'),
        }
        return render(request, self.template_name, context)


class ItemsListView(ListView):
    template_name = 'statistic/items_stat.html'
    context_object_name = 'items'
    queryset = catalog.models.Item.objects.all()


class ItemsStatisticsView(DetailView):
    template_name = 'statistic/items_stat.html'

    def get(self, request, *args, **kwargs):
        ratings_count = rating.models.Rating.objects.get_items_ratings_count(
            self.kwargs['pk']
        )
        ratings_avg = rating.models.Rating.objects.get_items_ratings_avg(
            self.kwargs['pk']
        )
        top_rater = rating.models.Rating.objects.get_item_top_rater(
            self.kwargs['pk']
        )
        bottom_rater = rating.models.Rating.objects.get_item_bottom_rater(
            self.kwargs['pk']
        )
        context = {
            'ratings_count': ratings_count.get('ratings_count'),
            'ratings_avg': ratings_avg.get('ratings_avg'),
            'top_rater': top_rater,
            'bottom_rater': bottom_rater,
        }
        return render(request, self.template_name, context)


class UserItemsStat(ListView, LoginRequiredMixin):
    template_name = 'statistic/user_items_stat.html'

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        # здесь достается queryset из объектов Rating. В шаблоне будешь
        # доставать оценку через rating.rating, а сам Item через rating.item
        items_list = catalog.models.Item.objects.get_users_items_list(user_id)
        context = {
            'ratings': items_list,
        }
        return render(request, self.template_name, context)
