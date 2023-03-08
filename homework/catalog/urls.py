from django.urls import path, re_path, register_converter

from catalog import converters, views

register_converter(converters.PositiveInteger, 'posint')

app_name = 'catalog'
urlpatterns = [
    path('', views.item_list, name='item-list'),
    path('<int:pk>/', views.item_detail, name='item-detail'),
    path(
        'converter/<posint:pk>',
        views.item_detail,
        name='postitive-number-check',
    ),
    path(
        'download-main-image/<posint:item_pk>',
        views.download_main_image,
        name='download-main-image',
    ),
    path(
        'download-gallery-image/<posint:image_pk>',
        views.download_gallery_image,
        name='download-gallery-image',
    ),
    path(
        'new-items',
        views.new_items,
        name='new-items',
    ),
    path(
        'friday-items',
        views.friday_items,
        name='friday-items',
    ),
    path(
        'unchanged-items',
        views.unchanged_items,
        name='unchanged-items',
    ),
    re_path(
        r're/(?P<pk>[1-9]\d*)/$',
        views.item_detail,
        name='re-positive-number-check',
    ),
]
