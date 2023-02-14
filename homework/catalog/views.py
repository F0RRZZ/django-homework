from django.http import HttpResponse


def item_list(request):
    return HttpResponse('<body>Список элементов</body>')


def item_detail(request, pk):
    return HttpResponse(f'<body>Число {pk}</body>')
