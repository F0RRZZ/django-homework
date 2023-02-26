from django.contrib import admin

import catalog.models


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Category.name.field.name,
        catalog.models.Category.is_published.field.name,
    )
    exclude = (catalog.models.Category.formatted_name.field.name,)
    list_editable = (catalog.models.Category.is_published.field.name,)
    list_display_links = (catalog.models.Category.name.field.name,)


class GalleryImageInline(admin.TabularInline):
    model = catalog.models.GalleryImage


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [
        GalleryImageInline,
    ]
    filter_horizontal = ('tags',)
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
        'image_thumbnail',
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Tag.name.field.name,
        catalog.models.Tag.is_published.field.name,
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Tag.name.field.name,)
