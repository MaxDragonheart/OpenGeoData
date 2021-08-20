from django.contrib import admin

from .models import UrbanisticaContenuti, UrbanisticaCategorie
from abstracts.admin import CategoryBaseAdmin, ModelPostBaseAdmin


class UrbanisticaCategorieAdmin(CategoryBaseAdmin):
    fieldsets = [
                (None, {"fields": ["category_name", "slug_category", "description"]}),
            ]

    class Meta:
        model = UrbanisticaCategorie


class UrbanisticaContenutiAdmin(ModelPostBaseAdmin):
    fieldsets = [
        (None, {"fields": ["title", "slug_post", "header_image"]}),
        ("Contenuti", {"fields": ["description", "contents"]}),
        ("Riferimenti", {"fields": ["publishing_date", "category", "urbanistica_sharedtags"]}),
        ("Opzioni", {"fields": ["highlighted", "draft"]}),
    ]

    class Meta:
        model = UrbanisticaContenuti


admin.site.register(UrbanisticaCategorie, UrbanisticaCategorieAdmin)
admin.site.register(UrbanisticaContenuti, UrbanisticaContenutiAdmin)