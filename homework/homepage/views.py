from http import HTTPStatus

from django.http import HttpResponse

homepage_title = 'Главная'


def home(request):
    return HttpResponse(homepage_title)


def teapot_status_page(request):
    return HttpResponse('Я чайник', status=HTTPStatus.IM_A_TEAPOT)
