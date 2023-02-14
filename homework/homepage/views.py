from http import HTTPStatus

from django.http import HttpResponse


def home(request):
    return HttpResponse('<body>Главная</body>')


def teapot_status_page(request):
    return HttpResponse('<body>Я чайник</body>', status=HTTPStatus.IM_A_TEAPOT)
