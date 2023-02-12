from django.http import HttpResponse


def item_list(request):
    return HttpResponse('<body>Список элементов</body>')


def item_detail(request, item):
    return HttpResponse(f'<body>Подробно об элементе {item}</body>')


def catalog_re(request, number):
    return HttpResponse(f'<body>Number: {number}</body>')


def positive_number(request, number):
    return HttpResponse(f'<body>Positive integer</body>')
