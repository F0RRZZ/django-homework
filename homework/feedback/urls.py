from django.urls import path

from feedback import views

app_name = 'feedback'
urlpatterns = [
    path('', views.feedback_form, name='feedback'),
    path('success/', views.success, name='success'),
]
