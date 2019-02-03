from django.contrib import admin

from .models import Brand, Guitar


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Guitar)
class GuitarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('model_name',)}
