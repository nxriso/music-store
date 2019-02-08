from django.contrib import admin

from . import models


@admin.register(models.FamousClients)
class FamousClientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']
