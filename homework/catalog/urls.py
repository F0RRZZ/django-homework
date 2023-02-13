from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.PositiveInteger, 'posint')

app_name = 'catalog'
urlpatterns = [
    path('', views.item_list, name='item-list'),
    path('<int:item>/', views.item_detail, name='item-detail'),
    path(
        'converter/<posint:number>',
        views.positive_number,
        name='postitive-number-check',
    ),
    re_path(
        r're/(?P<number>\d+)',
        views.catalog_re,
        name='re-positive-number-check',
    ),
]
