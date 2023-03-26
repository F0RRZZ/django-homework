from datetime import timedelta

from django.http import HttpResponse
import django.shortcuts
from django.utils import timezone
from django.views.generic import DetailView, ListView, FormView, TemplateView

import catalog.forms
import catalog.models
import core.rating.base_views
import rating.models


class ItemListView(ListView):
    template_name = 'catalog/list.html'
    context_object_name = 'categories'
    queryset = catalog.models.Category.objects.published()


class ItemDetailView(FormView):
    template_name = 'catalog/item.html'
    form_class = catalog.forms.RatingForm
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = catalog.models.Item.objects.get_with_rating(
            self.kwargs.get(self.pk_url_kwarg),
        )
        return context

    def form_valid(self, form):
        user_id = self.request.user.id
        item_id = self.kwargs.get(self.pk_url_kwarg)
        rating_ = form.cleaned_data[rating.models.Rating.rating.field.name]

        rating_object = rating.models.Rating.objects.filter(
            user_id=user_id, item_id=item_id
        ).first()
        if rating_object:
            if rating_ is None:
                rating_object.delete()
            else:
                rating_object.rating = rating_
                rating_object.save()
        elif rating_ is not None:
            rating.models.Rating.objects.create(
                rating=rating_,
                user_id=user_id,
                item_id=item_id,
            )
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            rating_object = rating.models.Rating.objects.filter(
                user_id=self.request.user.id,
                item_id=self.kwargs.get(self.pk_url_kwarg),
            ).first()
            if rating_object:
                initial[
                    rating.models.Rating.rating.field.name
                ] = rating_object.rating
        return initial

    def get_success_url(self):
        return '/catalog/{}/'.format(self.kwargs.get(self.pk_url_kwarg))


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
