from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render

homepage_title = 'Главная'


def home(request):
    template = 'homepage/homepage.html'
    context = {}
    return render(request, template, context)


def teapot_status_page(request):
    return HttpResponse('Я чайник', status=HTTPStatus.IM_A_TEAPOT)
