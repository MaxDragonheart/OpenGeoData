from django.contrib import admin

from .models import GeoServerURL, WMSLayer, BasemapProvider, Basemap, WebGISProject


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
                (None, {"fields": ["title", "slug_post", "description"]}),
                ("WMS Parameters", {"fields": ["wms_layer_path", "wms_layer_name", "wms_layer_style"]}),
                ("OpenLayers Parameters",
                 {"fields": ["set_max_zoom", "set_min_zoom", "set_zindex", "set_opacity"]}
                 ),
            ]

    class Meta:
        model = WMSLayer


class BasemapProviderAdmin(admin.ModelAdmin):
    list_display = ["name", "raw_url"]

    class Meta:
        model = BasemapProvider


class BasemapAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "provider", "url", "thumbnail"]
    list_filter = ["provider"]

    class Meta:
        model = Basemap


class WebGISProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "publishing_date", "updating_date", "highlighted", "draft"]
    list_filter = ["publishing_date"]
    search_fields = ["title"]
    prepopulated_fields = {"slug_post": ("title",)}
    fieldsets = [
                (None, {"fields": ["title", "slug_post", "header_image", "description"]}),
                (None, {"fields": ["contents"]}),
                (None, {"fields": ["draft", "highlighted", "publishing_date"]}),
                ("Basemap", {"fields": ["basemap1", "basemap2", "basemap3"]}),
                ("OpenLayers Parameters",
                 {
                     "classes": ("collapse",),
                     "fields":
                      ["map_scaleline", "map_attribution", "map_center_longitude",
                       "map_center_latitude", "set_max_zoom", "set_min_zoom", "set_zoom_level"
                       ]
                  }
                 ),
                ("WMS Layer",  {"fields": ["layers"]}),
            ]

    class Meta:
        model = WebGISProject


admin.site.register(GeoServerURL, GeoServerURLAdmin)
admin.site.register(WMSLayer, WMSLayerAdmin)
admin.site.register(BasemapProvider, BasemapProviderAdmin)
admin.site.register(Basemap, BasemapAdmin)
admin.site.register(WebGISProject, WebGISProjectAdmin)