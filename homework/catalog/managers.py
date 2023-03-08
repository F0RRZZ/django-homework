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
                'name',
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
                    ).only('name'),
                )
            )
            .only(
                'id',
                'name',
                'category__name',
                'text',
            )
            .order_by(
                'name',
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
                    ).only('name'),
                )
            )
            .only(
                'id',
                'name',
                'category__name',
                'text',
            )
            .order_by(
                'category__name',
                'name',
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
                    ).only('name'),
                ),
                django.db.models.Prefetch(
                    'galleryimage_set',
                ),
            )
            .only(
                'name',
                'category__name',
                'text',
            )
        )
