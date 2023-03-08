from datetime import timedelta

import django.db.models
from django.http import HttpResponse
import django.shortcuts
from django.utils import timezone

import catalog.models


def item_list(request):
    template = 'catalog/list.html'
    categories = catalog.models.Category.objects.published()
    context = {
        'categories': categories,
    }
    return django.shortcuts.render(request, template, context)


def item_detail(request, pk):
    template = 'catalog/item.html'
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item.objects.description(pk)
    )
    context = {
        'item': item,
    }
    return django.shortcuts.render(request, template, context)


def download_main_image(request, item_pk):
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item.objects.filter(pk=item_pk, is_published=True)
    )
    response = HttpResponse(item.main_image.image, content_type='image')
    response['Content-Disposition'] = (
        f'attachment;' f' filename="{item.main_image.image}"'
    )
    return response


def download_gallery_image(request, image_pk):
    image = django.shortcuts.get_object_or_404(
        catalog.models.GalleryImage.objects.filter(pk=image_pk)
    )
    response = HttpResponse(image.image, content_type='image')
    response['Content-Disposition'] = (
        f'attachment; ' f'filename="{image.image}"'
    )
    return response


def new_items(request):
    template = 'catalog/items_list_by_date.html'
    one_week_ago = timezone.now() - timedelta(weeks=1)
    items = catalog.models.Item.objects.new(one_week_ago)
    context = {'sort_type': 'Новинки', 'items': items}
    return django.shortcuts.render(request, template, context)


def friday_items(request):
    template = 'catalog/items_list_by_date.html'
    items = catalog.models.Item.objects.updated_on_friday()
    context = {'sort_type': 'Пятница', 'items': items}
    return django.shortcuts.render(request, template, context)


def unchanged_items(request):
    template = 'catalog/items_list_by_date.html'
    items = catalog.models.Item.objects.unchanged()
    context = {'sort_type': 'Непроверенное', 'items': items}
    return django.shortcuts.render(request, template, context)
