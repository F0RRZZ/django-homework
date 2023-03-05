from http import HTTPStatus

from django.http import HttpResponse

import django.shortcuts

import catalog.models

store_name = 'Some store'


def home(request):
    template = 'homepage/homepage.html'
    items = catalog.models.Item.objects.on_main()
    context = {
        'store_name': store_name,
        'items': items,
    }
    return django.shortcuts.render(request, template, context)


def teapot_status_page(request):
    return HttpResponse('Я чайник', status=HTTPStatus.IM_A_TEAPOT)
