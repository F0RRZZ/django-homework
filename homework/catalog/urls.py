from django.urls import path, re_path, register_converter

from . import converters, views

register_converter(converters.PositiveInteger, 'posint')

urlpatterns = [
    path('', views.item_list),
    path('<int:item>/', views.item_detail),
    path('converter/<posint:number>', views.positive_number),
    re_path(r're/(?P<number>\d+)', views.catalog_re),
]
