from django.contrib import admin

from .models import GeoServerURL, OGCLayer, BasemapProvider, Basemap, WebGISProject


class GeoServerURLAdmin(admin.ModelAdmin):
    list_display = ["geoserver_domain", "geoserver_workspace", "publishing_date", "complete_url_wms", "complete_url_wfs"]
    search_fields = ["geoserver_domain", "geoserver_workspace"]

    class Meta:
        model = GeoServerURL


class OGCLayerAdmin(admin.ModelAdmin):
    list_display = ["title", "ogc_layer_name", "publishing_date", "ogc_bbox", "ogc_centroid", "header_image"]
    list_filter = ["publishing_date"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = [
                (None, {"fields": ["title", "slug", "description", "categories"]}),
                ("OGC Parameters", {"fields": [
                    "ogc_layer_path", "ogc_layer_name", "ogc_layer_style", "ogc_legend", "is_vector", "is_raster",
                ]}),
                #("OGC Extras", {"fields": ["header_image"]}),
                ("OpenLayers Parameters",
                 {"fields": ["set_max_zoom", "set_min_zoom", "set_zindex", "set_opacity"]}
                 ),
            ]

    class Meta:
        model = OGCLayer


class WebGISProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "publishing_date", "updating_date", "highlighted", "draft"]
    list_filter = ["publishing_date"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = [
                ("Header", {"fields": ["title", "slug", "header_image", "description"]}),
                ("Contents", {"fields": ["contents", "categories"]}),
                ("Options", {"fields": ["draft", "highlighted", "publishing_date"]}),
                #("Basemap", {"fields": ["basemap1", "basemap2", "basemap3"]}),
                ("OpenLayers Parameters",
                 {
                     "classes": ("collapse",),
                     "fields":
                      ["map_scaleline", "map_attribution", "map_center_longitude",
                       "map_center_latitude", "set_max_zoom", "set_min_zoom", "set_zoom_level"
                       ]
                  }
                 ),
                ("OGC Layer",  {"fields": ["main_layer", "layers"]}),
            ]

    class Meta:
        model = WebGISProject


class BasemapProviderAdmin(admin.ModelAdmin):
    list_display = ["name", "raw_url"]

    class Meta:
        model = BasemapProvider


class BasemapAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "provider", "url", "thumbnail"]
    list_filter = ["provider"]

    class Meta:
        model = Basemap


admin.site.register(GeoServerURL, GeoServerURLAdmin)
admin.site.register(OGCLayer, OGCLayerAdmin)
admin.site.register(WebGISProject, WebGISProjectAdmin)
# admin.site.register(BasemapProvider, BasemapProviderAdmin)
# admin.site.register(Basemap, BasemapAdmin)
