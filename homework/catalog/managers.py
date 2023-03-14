import django.db.models
from django.db.models import F
from django.db.models.functions import Trunc

import catalog.models


class CategoryManager(django.db.models.Manager):
    def published(self):
        return (
            self.get_queryset()
            .filter(
                is_published=True,
            )
            .order_by(
                catalog.models.Category.name.field.name,
            )
        )


class ItemManager(django.db.models.Manager):
    def on_main(self):
        return (
            self.get_queryset()
            .filter(
                is_published=True,
                is_on_main=True,
                category__is_published=True,
            )
            .select_related(
                'category',
            )
            .prefetch_related(
                django.db.models.Prefetch(
                    'tags',
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True,
                    ).only(catalog.models.Tag.name.field.name),
                )
            )
            .only(
                'id',
                catalog.models.Item.name.field.name,
                f'{catalog.models.Item.category.field.name}__'
                f'{catalog.models.Category.name.field.name}',
                catalog.models.Item.text.field.name,
            )
            .order_by(
                catalog.models.Item.text.field.name,
            )
        )

    def published(self):
        return (
            self.get_queryset()
            .filter(is_published=True, category__is_published=True)
            .prefetch_related(
                django.db.models.Prefetch(
                    'tags',
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True,
                    ).only(catalog.models.Tag.name.field.name),
                ),
                django.db.models.Prefetch(
                    'main_image',
                    queryset=catalog.models.MainImage.objects.only(
                        catalog.models.MainImage.image.field.name
                    ),
                ),
            )
            .only(
                'id',
                catalog.models.Item.name.field.name,
                f'{catalog.models.Item.category.field.name}__'
                f'{catalog.models.Category.name.field.name}',
                catalog.models.Item.text.field.name,
            )
            .order_by(
                f'{catalog.models.Item.category.field.name}__'
                f'{catalog.models.Category.name.field.name}',
                catalog.models.Item.name.field.name,
            )
        )

    def description(self, pk):
        return (
            self.get_queryset()
            .filter(
                pk=pk,
                is_published=True,
                category__is_published=True,
            )
            .prefetch_related(
                django.db.models.Prefetch(
                    'tags',
                    queryset=catalog.models.Tag.objects.filter(
                        is_published=True,
                    ).only(catalog.models.Tag.name.field.name),
                ),
                django.db.models.Prefetch(
                    'galleryimage_set',
                ),
            )
            .only(
                catalog.models.Item.name.field.name,
                f'{catalog.models.Item.category.field.name}__'
                f'{catalog.models.Category.name.field.name}',
                catalog.models.Item.text.field.name,
            )
        )

    def new(self, time):
        return (
            self.get_queryset()
            .filter(
                is_published=True,
                created_at__gte=time,
            )
            .order_by('?')[:5]
        )

    def updated_on_friday(self):
        return (
            self.get_queryset()
            .filter(
                is_published=True,
                updated_at__week_day=5,
            )
            .order_by('-updated_at')[:5]
        )

    def unchanged(self):
        return (
            self.get_queryset()
            .annotate(
                created=Trunc('created_at', 'second'),
                updated=Trunc('updated_at', 'second'),
            )
            .filter(
                is_published=True,
                created=F('updated'),
            )
            .order_by('created_at')
        )
