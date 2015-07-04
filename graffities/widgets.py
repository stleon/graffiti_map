from django import forms
from django.utils.safestring import mark_safe


class MapWidget(forms.RadioSelect):
    def render(self, name, value, attrs=None):
        html = super(MapWidget, self).render(name, value, attrs)
        html = '<div id="map" style="width:auto; height:300px"></div>%s' % html
        return mark_safe(html)

    class Media():
        js = ('js/jquery.min.js', 'js/yandex_map.js', 'js/add_map.js')
