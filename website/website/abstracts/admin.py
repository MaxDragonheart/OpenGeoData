from django.contrib import admin


class CategoryBaseAdmin(admin.ModelAdmin):
    """
    con questa classe definisco come viene gestito Category
    nell'admin panel
    """
    list_display = ["category_name"]
    prepopulated_fields = {"slug_category": ("category_name",)}


class TagBaseAdmin(admin.ModelAdmin):
    """
    con questa classe definisco come viene gestito KeyConcept
    nell'admin panel
    """
    list_display = ["tag_name", "publishing_date"]
    list_filter = ["publishing_date"]
    search_fields = ["tag_name"]
    prepopulated_fields = {"slug_tag": ("tag_name",)}
    fieldsets = [
                (None, {"fields": ["tag_name", "slug_tag"]}),
            ]


class ModelPostBaseAdmin(admin.ModelAdmin):
    """
    con questa classe definisco come viene gestito Blog
    nell'admin panel
    """
    list_display = ["title", "time_of_reading", "publishing_date", "updating_date", "highlighted", "draft", "is_future", "category"]
    list_filter = ["publishing_date", "updating_date", "category"]
    search_fields = ["title", "description", "contents"]
    prepopulated_fields = {"slug_post": ("title",)}


class UploadBaseAdmin(admin.ModelAdmin):
    list_filter = ["publishing_date"]
    search_fields = ["name", "description"]

