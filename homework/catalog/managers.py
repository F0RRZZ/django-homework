import django.db.models

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
                'category__name',
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
            .select_related('category')
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
                'category__name',
                catalog.models.Item.text.field.name,
            )
            .order_by(
                'category__name',
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
                'category__name',
                catalog.models.Item.text.field.name,
            )
        )
