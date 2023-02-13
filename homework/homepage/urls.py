from django.urls import path

from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.home, name='index'),
    path('coffee/', views.teapot_error, name='teapot-error'),
]
