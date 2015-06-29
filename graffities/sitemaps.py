from django.contrib.sitemaps import Sitemap
from .models import Graffiti

class GraffitiSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return Graffiti.objects.filter(active=True, checked=True)

    def lastmod(self, obj):
        return obj.date_updated
