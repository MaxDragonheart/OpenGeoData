import datetime
from pathlib import Path

from django.conf import settings
from django.contrib.gis.db import models
from django.urls import reverse

from abstracts.models import TimeManager, BaseModelPost, ModelPost
from fsspec import get_fs_token_paths

from .utils import get_wms_bbox, get_centroid_coords, get_wms_thumbnail, WMS_THUMBNAILS


class OpenLayersMapParameters(models.Model):
    map_scaleline = models.BooleanField(default=True)
    map_attribution = models.CharField(max_length=250, default='<a href="https://massimilianomoraca.it/" target="_blank">Massimiliano Moraca</a> has created this map using <a href="https://openlayers.org/" target="_blank">OpenLayers</a>')
    map_center_longitude = models.DecimalField(max_digits=10, decimal_places=5, default=14.239649)
    map_center_latitude = models.DecimalField(max_digits=10, decimal_places=5, default=40.842906)
    set_max_zoom = models.IntegerField(default=28)
    set_min_zoom = models.IntegerField(default=0)
    set_zoom_level = models.IntegerField(default=0)

    class Meta:
        abstract = True


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


class WMSLayer(BaseModelPost, OpenLayersMapParameters):
    set_zindex = models.IntegerField(default=1)
    set_opacity = models.DecimalField(max_digits=3, decimal_places=2, default=1.0)
    wms_layer_path = models.ForeignKey(GeoServerURL, related_name="related_geoserver_url", on_delete=models.PROTECT, blank=True, null=True)
    wms_layer_name = models.CharField(max_length=100)
    wms_layer_style = models.CharField(max_length=100, blank=True, null=True)
    wms_bbox = models.CharField(max_length=250, blank=True, null=True)
    wms_centroid = models.CharField(max_length=250, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("wms-single", kwargs={"slug_post": self.slug_post})

    def save(self, *args, **kwargs):
        """Override save method and add to DB thumbnail path, BBOX and centroid"""

        # Create the thumbnail destination folder
        today = datetime.datetime.now()
        today_folder = Path(f"{today.year}/{today.month}/{today.day}")
        output_folder = settings.MEDIA_FOLDER / WMS_THUMBNAILS
        destination_folder = output_folder / today_folder
        fs, fs_token, paths = get_fs_token_paths(destination_folder)
        fs.mkdirs(path=destination_folder, exist_ok=True)

        # Get thumbnail from WMS
        img_path = get_wms_thumbnail(
            wms_url=self.wms_layer_path.complete_url_wms,
            service_version="1.3.0",
            layer_name=self.wms_layer_name,
            output_data_folder=destination_folder,
        )
        self.header_image = f"{WMS_THUMBNAILS}/{today_folder}/{img_path.stem}{img_path.suffix}"

        # Get WMS's BBOX
        self.wms_bbox = list(get_wms_bbox(
            wms_url=self.wms_layer_path.complete_url_wms,
            service_version="1.3.0",
            layer_name=self.wms_layer_name
        ))

        # Get BBOX's centroid
        self.wms_centroid = list(get_centroid_coords(self.wms_bbox))

        # Save all
        super(WMSLayer, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "WMS Layer"
        verbose_name_plural = "WMS Layers"


class BasemapProvider(TimeManager):
    name = models.CharField(max_length=250, unique=True)
    user = models.CharField(max_length=250, blank=True, null=True)
    token = models.CharField(max_length=250, blank=True, null=True)
    raw_url = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "Basemap Provider"
        verbose_name_plural = "Basemap Provider"


class Basemap(TimeManager):
    title = models.CharField(max_length=250)
    provider = models.ForeignKey(BasemapProvider, on_delete=models.CASCADE, related_name="releted_basemap_provider")
    tile_code = models.CharField(max_length=250, blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Make basemap url"""
        raw_url = self.provider.raw_url
        print(f"Basemap Provider: {self.provider.name}")
        if self.provider.user:
            user_url = raw_url.replace('USER', self.provider.user)
        else:
            user_url = raw_url

        tilecode_url = user_url.replace('TILECODE', self.tile_code)
        self.url = tilecode_url.replace('TOKEN', self.provider.token)
        super(Basemap, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "Basemap"
        verbose_name_plural = "Basemap"


class WebGISProjectBase(ModelPost, OpenLayersMapParameters):

    class Meta:
        abstract = True


class WebGISProject(WebGISProjectBase):
    #tags = models.ManyToManyField(WebGISProjectTag, related_name="related_webgisprojecttag")
    #basemap_layers = models.BooleanField(default=False)
    #basemap = models.ManyToManyField(Basemap, related_name="related_basemap", blank=True)
    #basemaps = models.ForeignKey(Basemap, on_delete=models.PROTECT, related_name="related_basemap")
    layers = models.ManyToManyField(WMSLayer, related_name="related_wmslayer", blank=True)

    def get_absolute_url(self):
        return reverse("map-single", kwargs={"slug_post": self.slug_post})

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "WebGIS"
        verbose_name_plural = "WebGIS"