from django.contrib import admin

from .models import Brand, Guitar


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Guitar)
class GuitarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('model_name',)}
