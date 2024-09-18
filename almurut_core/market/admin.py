from django.contrib import admin
from django.utils.html import format_html

from market.models import Product, ProductCategory, ProductGallery



@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]




class ProductGalleryInlineAdmin(admin.StackedInline):
    model = ProductGallery
    extra = 4



@admin.register(Product)
class ProductGalerry(admin.ModelAdmin):
    list_display = ['name', 'price', 'seles_persent',]
    search_fields = ['name',]
    inlines = [ProductGalleryInlineAdmin]

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100"/>'. format(obj.preview_image.url))

    image_tag.short_description = 'Превью-изображения '






