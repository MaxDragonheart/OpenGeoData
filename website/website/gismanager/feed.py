from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed


from .models import OGCLayer, WebGISProject


class FeedBase(Feed):
    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.publishing_date

    def item_updateddate(self, item):
        return item.updating_date

    def item_description(self, item):
        return item.description


class FeedOGCLayer(FeedBase):
    title = "Nuovo layer OGC"
    link = ""
    description = "Ultime news"

    def items(self):
        return OGCLayer.objects.all().order_by('-publishing_date')[:5]


class AtomOGCLayer(FeedOGCLayer):
    feed_type = Atom1Feed
    subtitle = FeedOGCLayer.description


class FeedWebGISProject(FeedBase):
    title = "Nuovo webgis"
    link = ""
    description = "Ultime news"

    def items(self):
        return WebGISProject.objects.all().order_by('-publishing_date')[:5]


class AtomWebGISProject(FeedWebGISProject):
    feed_type = Atom1Feed
    subtitle = FeedWebGISProject.description

