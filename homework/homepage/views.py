from http import HTTPStatus

from django.http import HttpResponse


def home(request):
    return HttpResponse('Главная')


def teapot_status_page(request):
    return HttpResponse('Я чайник', status=HTTPStatus.IM_A_TEAPOT)
