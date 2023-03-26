from django.urls import path, re_path, register_converter

from catalog import converters, views

register_converter(converters.PositiveInteger, 'posint')

app_name = 'catalog'
urlpatterns = [
    path('', views.ItemListView.as_view(), name='item-list'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path(
        'converter/<posint:pk>',
        views.ItemDetailView.as_view(),
        name='postitive-number-check',
    ),
    path(
        'download-main-image/<posint:pk>',
        views.DownloadMainImageView.as_view(),
        name='download-main-image',
    ),
    path(
        'download-gallery-image/<posint:pk>',
        views.DownloadGalleryImageView.as_view(),
        name='download-gallery-image',
    ),
    path(
        'new-items',
        views.NewItemsView.as_view(),
        name='new-items',
    ),
    path(
        'friday-items',
        views.FridayItemsView.as_view(),
        name='friday-items',
    ),
    path(
        'unchanged-items',
        views.UnchangedItemsView.as_view(),
        name='unchanged-items',
    ),
    re_path(
        r're/(?P<pk>[1-9]\d*)/$',
        views.ItemDetailView.as_view(),
        name='re-positive-number-check',
    ),
]
