from django.conf import settings
from django.contrib.gis.db import models
from django.urls import reverse

from abstracts.models import TimeManager, BaseModelPost

from .utils import get_wms_bbox, get_centroid_coords, get_wms_thumbnail


class GeoServerURL(TimeManager):
    geoserver_domain = models.URLField(unique=True)
    geoserver_workspace = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.geoserver_domain}/geoserver/{self.geoserver_workspace}/"

    @property
    def complete_url_wms(self):
        return f"{self.geoserver_domain}/geoserver/{self.geoserver_workspace}/wms"

    @property
    def complete_url_wfs(self):
        return f"{self.geoserver_domain}/geoserver/{self.geoserver_workspace}/wfs"

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "GeoServer URL"
        verbose_name_plural = "GeoServer URL"


class WMSLayer(BaseModelPost):
    wms_layer_path = models.ForeignKey(GeoServerURL, related_name="related_geoserver_url", on_delete=models.PROTECT, blank=True, null=True)
    wms_layer_name = models.CharField(max_length=100)
    wms_layer_style = models.CharField(max_length=100, blank=True, null=True)
    set_max_zoom = models.IntegerField(default=28)
    set_min_zoom = models.IntegerField(default=0)
    set_zindex = models.IntegerField(default=1)
    set_opacity = models.DecimalField(max_digits=3, decimal_places=2, default=1.0)
    wms_bbox = models.CharField(max_length=250, blank=True, null=True)
    wms_centroid = models.CharField(max_length=250, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("webgislayer_single", kwargs={"slug_post": self.slug_post})

    def save(self, *args, **kwargs):
        img_path = get_wms_thumbnail(
            wms_url=self.wms_layer_path.complete_url_wms,
            service_version="1.3.0",
            layer_name=self.wms_layer_name,
            output_data_folder=settings.WMS_THUMBNAILS,
        )
        print(img_path)
        self.header_image = str(img_path)
        self.wms_bbox = get_wms_bbox(
            wms_url=self.wms_layer_path.complete_url_wms,
            service_version="1.3.0",
            layer_name=self.wms_layer_name
        )
        self.wms_centroid = get_centroid_coords(self.wms_bbox)
        super(WMSLayer, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "WMS Layer"
        verbose_name_plural = "WMS Layers"