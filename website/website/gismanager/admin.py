from django.contrib import admin

from .models import GeoServerURL, WMSLayer


class GeoServerURLAdmin(admin.ModelAdmin):
    list_display = ["geoserver_domain", "geoserver_workspace", "publishing_date", "complete_url_wms", "complete_url_wfs"]
    search_fields = ["geoserver_domain", "geoserver_workspace"]

    class Meta:
        model = GeoServerURL


class WMSLayerAdmin(admin.ModelAdmin):
    list_display = ["title", "wms_layer_name", "publishing_date", "wms_bbox", "wms_centroid", "header_image"]
    list_filter = ["publishing_date"]
    search_fields = ["title"]
    prepopulated_fields = {"slug_post": ("title",)}
    fieldsets = [
                (None, {"fields": ["title", "slug_post", "header_image"]}),
                (None, {"fields": ["description", "publishing_date"]}),
                ("WMS Parameters", {"fields": ["wms_layer_path", "wms_layer_name", "wms_layer_style"]}),
                ("OpenLayers Parameters",
                 {"fields": ["set_max_zoom", "set_min_zoom", "set_zindex", "set_opacity"]}
                 ),
            ]

    class Meta:
        model = WMSLayer


admin.site.register(GeoServerURL, GeoServerURLAdmin)
admin.site.register(WMSLayer, WMSLayerAdmin)