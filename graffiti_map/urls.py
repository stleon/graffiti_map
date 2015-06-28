from django.conf.urls import include, url
from django.contrib import admin
from .settings import PROJECT_NAME, DEBUG, MEDIA_ROOT

# Настройка админки

#admin.site.site_url = "http://127.0.0.1"
admin.site.site_header = PROJECT_NAME
admin.site.site_title = PROJECT_NAME
admin.site.index_title = 'Администрирование'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('graffities.urls')),
    ]

if DEBUG:
    urlpatterns += [
        url(r'^datastore/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT,
        }),
   ]
