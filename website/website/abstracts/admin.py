from django.contrib import admin


class CategoryBaseAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug": ("title",)}


class TagBaseAdmin(admin.ModelAdmin):
    list_display = ["title", "publishing_date"]
    list_filter = ["publishing_date"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}


class ModelPostBaseAdmin(admin.ModelAdmin):
    list_display = ["title", "time_of_reading", "publishing_date", "updating_date", "highlighted", "draft", "is_future", "category"]
    list_filter = ["publishing_date", "updating_date", "category"]
    search_fields = ["title", "description", "contents"]
    prepopulated_fields = {"slug": ("title",)}


class UploadBaseAdmin(admin.ModelAdmin):
    list_filter = ["publishing_date"]
    search_fields = ["name", "description"]

