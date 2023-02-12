from django.http import HttpResponse


def item_list(request):
    return HttpResponse('<body>Список элементов</body>')


def item_detail(request, item):
    return HttpResponse(f'<body>Подробно об элементе {item}</body>')
