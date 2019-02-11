from django.contrib import admin

from . import models


@admin.register(models.HomeSlide)
class HomeSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
