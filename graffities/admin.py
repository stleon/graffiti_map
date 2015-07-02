from django.contrib import admin
from .models import Graffiti

@admin.register(Graffiti)
class GraffitiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'lat', 'lon', 'date_created',
        'date_updated', 'active', 'checked',)
    list_filter = ['active', 'checked', 'legal', ]
    search_fields = ['name', 'lat', 'lon']
