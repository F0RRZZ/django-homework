from datetime import timedelta

from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import DetailView, ListView

import catalog.models
import core.rating.base_views


class ItemListView(ListView):
    template_name = 'catalog/list.html'
    context_object_name = 'categories'
    queryset = catalog.models.Category.objects.published()


class ItemDetailView(DetailView):
    model = catalog.models.Item
    template_name = 'catalog/item.html'
    context_object_name = 'item'
    pk_url_kwarg = 'pk'


class DownloadMainImageView(DetailView):
    model = catalog.models.Item
    queryset = catalog.models.Item.objects.filter(is_published=True)
    pk_url_kwarg = 'pk'

    def render_to_response(self, context, **response_kwargs):
        response = HttpResponse(
            context['object'].main_image.image, content_type='image'
        )
        response[
            'Content-Disposition'
        ] = f'attachment; filename="{context["object"].main_image.image}"'
        return response


class DownloadGalleryImageView(DetailView):
    model = catalog.models.GalleryImage
    queryset = catalog.models.GalleryImage.objects.all()
    pk_url_kwarg = 'pk'

    def render_to_response(self, context, **response_kwargs):
        image = context['object']
        response = HttpResponse(image.image, content_type='image')
        response[
            'Content-Disposition'
        ] = f'attachment; filename="{image.image}"'
        return response


class NewItemsView(core.rating.base_views.ItemListByDateBaseView):
    queryset = catalog.models.Item.objects.new(
        timezone.now() - timedelta(weeks=1)
    )
    sort_type = 'Новинки'


class FridayItemsView(core.rating.base_views.ItemListByDateBaseView):
    queryset = catalog.models.Item.objects.updated_on_friday()
    sort_type = 'Пятница'


class UnchangedItemsView(core.rating.base_views.ItemListByDateBaseView):
    queryset = catalog.models.Item.objects.unchanged()
    sort_type = 'Непроверенное'
