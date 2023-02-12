from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.item_list),
    path('<int:item>/', views.item_detail),
    re_path(r're/(?P<number>\d+)', views.catalog_re),
]
