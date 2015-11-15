from django.contrib import admin
from django import forms
from .models import Graffiti
from .widgets import MapWidget


@admin.register(Graffiti)
class GraffitiAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'photo',
                    'lat',
                    'lon',
                    'date_created',
                    'date_updated',
                    'active',
                    'checked', )
    list_filter = ['active', 'checked', 'legal', 'graffiti_type']
    search_fields = ['name', 'lat', 'lon']
    fieldsets = [
        (None, {'fields': ['photo']}),
        ('Информация', {'fields': ['name', 'comment', 'graffiti_type']}),
        ('Статус', {'fields': ['active', 'checked', 'legal']}),
        ('Координаты', {'fields': ['lat', 'lon']}),
        ('Карта', {'fields': ['ya_map']}),
    ]

    class form(forms.ModelForm):
        ya_map = forms.BooleanField(label='Карта',
                                    widget=MapWidget(),
                                    required=False, )
