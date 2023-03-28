from django.urls import path, re_path, register_converter

import statistic.views

app_name = 'statistic'

urlpatterns = [
    path('users/', statistic.views.UsersStat.as_view(), name='users'),
    path('items/', statistic.views.ItemsStat.as_view(), name='items'),
    path('my_ratings/', statistic.views.UserItemsStat.as_view(), name='user_ratings'),
]
