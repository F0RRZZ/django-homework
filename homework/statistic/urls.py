from django.urls import path

import statistic.views

app_name = 'statistic'

urlpatterns = [
    path('users/', statistic.views.UsersListView.as_view(), name='users_list'),
    path(
        'users/<int:pk>',
        statistic.views.UsersStatisticsView.as_view(),
        name='user_statistic',
    ),
    path(
        'items/',
        statistic.views.ItemsListView.as_view(),
        name='items_list',
    ),
    path(
        'items/<int:pk>',
        statistic.views.ItemsStatisticsView.as_view(),
        name='item_statistic',
    ),
    path(
        'my_ratings/',
        statistic.views.UserItemsStat.as_view(),
        name='user_ratings',
    ),
]
