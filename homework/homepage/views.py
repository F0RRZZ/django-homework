from http import HTTPStatus

from django.http import HttpResponse

import catalog.models
from django.views.generic import TemplateView

store_name = 'Some store'


class HomeView(TemplateView):
    template_name = 'homepage/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = catalog.models.Item.objects.on_main()
        context['store_name'] = store_name
        context['items'] = items
        return context


def teapot_status_page(request):
    return HttpResponse('Я чайник', status=HTTPStatus.IM_A_TEAPOT)
