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


class MainImageInline(admin.TabularInline):
    model = catalog.models.MainImage
    can_delete = True


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [
        MainImageInline,
        GalleryImageInline,
    ]
    readonly_fields = ('get_image',)
    filter_horizontal = ('tags',)
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
        'get_image',
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)

    @admin.display(ordering='main_image', description='Главное изображение')
    def get_image(self, obj):
        return obj.main_image.image_thumbnail()


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Tag.name.field.name,
        catalog.models.Tag.is_published.field.name,
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Tag.name.field.name,)
