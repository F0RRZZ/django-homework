from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('coffee/', views.teapot_status_page, name='teapot-error'),
]
