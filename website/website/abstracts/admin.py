from django.contrib import admin


class CategoryBaseAdmin(admin.ModelAdmin):
    """
    con questa classe definisco come viene gestito Category
    nell'admin panel
    """
    list_display = ["title"]
    prepopulated_fields = {"slug": ("title",)}


class TagBaseAdmin(admin.ModelAdmin):
    """
    con questa classe definisco come viene gestito KeyConcept
    nell'admin panel
    """
    list_display = ["title", "publishing_date"]
    list_filter = ["publishing_date"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    # fieldsets = [
    #             (None, {"fields": ["title", "slug"]}),
    #         ]


class ModelPostBaseAdmin(admin.ModelAdmin):
    """
    con questa classe definisco come viene gestito Blog
    nell'admin panel
    """
    list_display = ["title", "time_of_reading", "publishing_date", "updating_date", "highlighted", "draft", "is_future", "category"]
    list_filter = ["publishing_date", "updating_date", "category"]
    search_fields = ["title", "description", "contents"]
    prepopulated_fields = {"slug": ("title",)}


class UploadBaseAdmin(admin.ModelAdmin):
    list_filter = ["publishing_date"]
    search_fields = ["name", "description"]

