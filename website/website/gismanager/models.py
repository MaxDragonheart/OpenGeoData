import datetime
from pathlib import Path

from django.conf import settings
from django.contrib.gis.db import models
from django.urls import reverse

from abstracts.models import TimeManager, BaseModelPost, ModelPost
from base.models import SharedCategories
from fsspec import get_fs_token_paths

from .utils import get_wms_bbox, get_centroid_coords, get_wms_thumbnail, WMS_THUMBNAILS


class OpenLayersMapParameters(models.Model):
    """
    OpenLayersMapParameters Abstract Model define the map's parameters based on
    OpenLayers [Map object](https://openlayers.org/en/latest/apidoc/module-ol_Map-Map.html).
    """
    map_scaleline = models.BooleanField(default=True)
    map_attribution = models.CharField(max_length=250, default='<a href="https://massimilianomoraca.it/" target="_blank">Massimiliano Moraca</a> has created this map using <a href="https://openlayers.org/" target="_blank">OpenLayers</a>')
    map_center_longitude = models.DecimalField(max_digits=10, decimal_places=5, default=14.23964)
    map_center_latitude = models.DecimalField(max_digits=10, decimal_places=5, default=40.84290)
    set_max_zoom = models.IntegerField(default=28)
    set_min_zoom = models.IntegerField(default=0)
    set_zoom_level = models.IntegerField(default=0)

    class Meta:
        abstract = True


class GeoServerURL(TimeManager):
    """
    GeoServerURL Model inherits TimeManager, it is useful to
    create a Geoserver url object.
    e.g.:
        geoserver_domain='www.mygeoserver.me'
        geoserver_workspace='MyWorkSpace'

        Geoserver URL: 'www.mygeoserver.me/geoserver/MyWorkSpace'
        WMS: 'www.mygeoserver.me/geoserver/MyWorkSpace/wms'
        WFS: 'www.mygeoserver.me/geoserver/MyWorkSpace/wfs'
    """
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
        verbose_name = "Geoserver url"
        verbose_name_plural = "Geoserver urls"


class OGCLayer(BaseModelPost, OpenLayersMapParameters):
    """
    OGCLayer Model inherits from BaseModelPost and OpenLayersMapParameters. This
    model can build an OGC layer using the attributes from OpenLayers [Layer objectc](https://openlayers.org/en/latest/apidoc/module-ol_layer_Layer-Layer.html).
    """
    set_zindex = models.IntegerField(default=1)
    set_opacity = models.DecimalField(max_digits=3, decimal_places=2, default=1.0)
    ogc_layer_path = models.ForeignKey(GeoServerURL, related_name="related_geoserver_url", on_delete=models.PROTECT, blank=True, null=True)
    ogc_layer_name = models.CharField(max_length=100)
    ogc_layer_style = models.CharField(max_length=100, blank=True, null=True)
    ogc_bbox = models.CharField(max_length=250, blank=True, null=True)
    ogc_centroid = models.CharField(max_length=250, blank=True, null=True)
    ogc_legend = models.BooleanField(default=False)
    is_vector = models.BooleanField()
    is_raster = models.BooleanField()
    categories = models.ManyToManyField(SharedCategories, related_name="related_ogc_categories")

    def get_absolute_url(self):
        return reverse("ogc-single", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """Override save method and add to DB thumbnail path, BBOX and centroid.

        :param args:
        :param kwargs:
        :return:
        """
        # Create the thumbnail destination folder
        today = datetime.datetime.now()
        today_folder = Path(f"{today.year}/{today.month}/{today.day}")
        output_folder = settings.MEDIA_FOLDER / WMS_THUMBNAILS
        destination_folder = output_folder / today_folder
        fs, fs_token, paths = get_fs_token_paths(destination_folder)
        fs.mkdirs(path=destination_folder, exist_ok=True)

        # Get thumbnail from WMS
        img_path = get_wms_thumbnail(
            wms_url=self.ogc_layer_path.complete_url_wms,
            service_version="1.3.0",
            layer_name=self.ogc_layer_name,
            output_data_folder=destination_folder,
        )
        self.header_image = f"{WMS_THUMBNAILS}/{today_folder}/{img_path.stem}{img_path.suffix}"

        # Get WMS's BBOX
        self.ogc_bbox = list(get_wms_bbox(
            wms_url=self.ogc_layer_path.complete_url_wms,
            service_version="1.3.0",
            layer_name=self.ogc_layer_name
        ))

        # Get BBOX's centroid
        self.ogc_centroid = list(get_centroid_coords(self.ogc_bbox))

        # Save all
        super(OGCLayer, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "OGC Layer"
        verbose_name_plural = "OGC Layers"


class BasemapProvider(TimeManager):
    """
    BasemapProvider Model inherits TimeManager, it is useful to create
    a basemap provider object.
    There is an issue #28
    """
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
    """
    Basemap Model inherits TimeManager, it is useful to create
    a basemap object related to a basemap provider.
    There is an issue #28
    """
    title = models.CharField(max_length=250)
    provider = models.ForeignKey(BasemapProvider, on_delete=models.CASCADE, related_name="releted_basemap_provider")
    tile_code = models.CharField(max_length=250, blank=True, null=True)
    thumbnail = models.ImageField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Make basemap url.
        """
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
        verbose_name_plural = "Basemaps"


class WebGISProjectBase(ModelPost, OpenLayersMapParameters):
    """
    WebGISProjectBase Abstract Model collect ModelPost and OpenLayersMapParameters.
    """

    class Meta:
        abstract = True


class WebGISProject(WebGISProjectBase):
    """
    WebGISProject Model inherits WebGISProjectBase, it is useful to create a webgis.
    """
    categories = models.ManyToManyField(SharedCategories, related_name="related_webgisproject_categories")
    basemap1 = models.ForeignKey(Basemap, on_delete=models.PROTECT, related_name="related_basemap1", blank=False, null=True)
    basemap2 = models.ForeignKey(Basemap, on_delete=models.PROTECT, related_name="related_basemap2", blank=True, null=True)
    basemap3 = models.ForeignKey(Basemap, on_delete=models.PROTECT, related_name="related_basemap3", blank=True, null=True)
    main_layer = models.ForeignKey(OGCLayer, on_delete=models.PROTECT, related_name="related_main_wmslayer")
    layers = models.ManyToManyField(OGCLayer, related_name="related_wmslayer", blank=True)

    def get_absolute_url(self):
        return reverse("map-single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-publishing_date']
        verbose_name = "WebGIS"
        verbose_name_plural = "WebGIS"