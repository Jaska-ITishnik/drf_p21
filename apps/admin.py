from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from apps.models import Product, Category


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    list_display = 'id', 'name', 'price', 'discount', 'photo_display'

    @admin.display(description='PHOTO')
    def photo_display(self, obj: Product):
        img_url = obj.photo
        if img_url:
            return mark_safe(f"<img src={img_url.url} alt='img' width='40px' height='50px'")
        else:
            return 'None image'


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass