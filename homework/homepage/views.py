from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render

store_name = 'Some store'


def home(request):
    template = 'homepage/homepage.html'
    context = {'store_name': store_name}
    return render(request, template, context)


def teapot_status_page(request):
    return HttpResponse('Я чайник', status=HTTPStatus.IM_A_TEAPOT)
