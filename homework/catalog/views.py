import django.db.models
import django.shortcuts

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
