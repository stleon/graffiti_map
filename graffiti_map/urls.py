from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.sitemaps import views
from .settings import PROJECT_NAME, DEBUG, MEDIA_ROOT
from .sitemaps import StaticViewSitemap
from graffities.sitemaps import GraffitiSitemap
from django.views.decorators.cache import cache_page

# Настройка админки

#admin.site.site_url = "http://127.0.0.1"
admin.site.site_header = PROJECT_NAME
admin.site.site_title = PROJECT_NAME
admin.site.index_title = 'Администрирование'


# Sitemaps

sitemaps = dict(
    stranitsy = StaticViewSitemap,
    graffities = GraffitiSitemap,
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('graffities.urls')),
    url(r'^contacts$', TemplateView.as_view(template_name="contacts.html"),
        name='contacts'),
    url(r'^about$', TemplateView.as_view(template_name="about.html"),
        name='about'),
    url(r'^sitemap\.xml$', cache_page(600)(views.index), {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', cache_page(600)(views.sitemap),
        {'sitemaps': sitemaps}),
    ]

if DEBUG:
    urlpatterns += [
        url(r'^datastore/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT,
        }),
   ]
