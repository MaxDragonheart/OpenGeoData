from django.contrib import admin

from .models import ProtezioneCivileCategorie, ProtezioneCivileContenuti
from abstracts.admin import CategoryBaseAdmin, ModelPostBaseAdmin


class ProtezioneCivileCategorieAdmin(CategoryBaseAdmin):
    fieldsets = [
                (None, {"fields": ["category_name", "slug_category", "description"]}),
            ]

    class Meta:
        model = ProtezioneCivileCategorie


class ProtezioneCivileContenutiAdmin(ModelPostBaseAdmin):
    fieldsets = [
        (None, {"fields": ["title", "slug_post", "header_image"]}),
        ("Contenuti", {"fields": ["description", "contents"]}),
        ("Riferimenti", {"fields": ["publishing_date", "category", "protezione_civile_sharedtags"]}),
        ("Opzioni", {"fields": ["highlighted", "draft"]}),
    ]

    class Meta:
        model = ProtezioneCivileContenuti


admin.site.register(ProtezioneCivileCategorie, ProtezioneCivileCategorieAdmin)
admin.site.register(ProtezioneCivileContenuti, ProtezioneCivileContenutiAdmin)