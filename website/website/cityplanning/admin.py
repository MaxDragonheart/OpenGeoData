from django.contrib import admin

from .models import CityPlanningCategory, CityPlannningPost
from abstracts.admin import CategoryBaseAdmin, ModelPostBaseAdmin


class CityPlanningCategoryAdmin(CategoryBaseAdmin):
    fieldsets = [
                (None, {"fields": ["category_name", "slug_category", "description"]}),
            ]

    class Meta:
        model = CityPlanningCategory


class CityPlannningPostAdmin(ModelPostBaseAdmin):
    fieldsets = [
        (None, {"fields": ["title", "slug_post", "header_image"]}),
        ("Contenuti", {"fields": ["description", "contents"]}),
        ("Riferimenti", {"fields": ["publishing_date", "category", "tags"]}),
        ("Opzioni", {"fields": ["attachment", "highlighted", "draft"]}),
    ]

    class Meta:
        model = CityPlannningPost


admin.site.register(CityPlanningCategory, CityPlanningCategoryAdmin)
admin.site.register(CityPlannningPost, CityPlannningPostAdmin)