from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.PositiveInteger, 'posint')

app_name = 'catalog'
urlpatterns = [
    path('', views.item_list, name='item-list'),
    path('<int:item>/', views.item_detail, name='item-detail'),
    path(
        'converter/<posint:number>',
        views.item_detail,
        name='postitive-number-check',
    ),
    re_path(
        r're/(?P<number>[1-9]\d*)/$',
        views.item_detail,
        name='re-positive-number-check',
    ),
]
