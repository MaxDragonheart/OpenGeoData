from django.contrib.sitemaps import ping_google, Sitemap
from django.contrib.flatpages.models import FlatPage
from django.urls import reverse

from base.models import SharedCategories
from gismanager.models import OGCLayer, WebGISProject


class CoreSitemap(Sitemap):
    """
    Generic Sitemap class.
    """
    protocol = "https"

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass


class CoreSitemap4Models(CoreSitemap):
    """
    Sitemap class for models.
    """

    def lastmod(self, obj):
        return obj.updating_date


######STATIC PAGE
class StaticSitemap(CoreSitemap):

    def items(self):
        return [
            'index',
            'wms-list', 'map',
        ]

    def location(self, item):
        return reverse(item)


######BASE
class SharedCategoriesSitemap(CoreSitemap4Models):

    def items(self):
        return SharedCategories.objects.all()


######GISMANAGER
class OGCLayerSitemap(CoreSitemap4Models):

    def items(self):
        return OGCLayer.objects.all()


class WebGISProjectSitemap(CoreSitemap4Models):

    def items(self):
        return WebGISProject.objects.all()
