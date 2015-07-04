from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['about', 'contacts']

    def location(self, item):
        return reverse(item)
