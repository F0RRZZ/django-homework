from django.views.generic import ListView


class ItemListByDateBaseView(ListView):
    template_name = 'catalog/items_list_by_date.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_type'] = self.sort_type
        return context
