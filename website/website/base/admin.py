from django.contrib import admin

from .models import SharedCategories, SiteCustomization, FileUpload, SiteUrls, SiteSocialUrls, Organogram


class SharedTagsAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "is_active", "publishing_date"]
    list_filter = ["is_active"]
    search_fields = ["title", "description"]
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = [
                (None, {"fields": ["title", "slug", "description", "icon", "is_active"]}),
            ]

    class Meta:
        model = SharedCategories


class SiteCustomizationAdmin(admin.ModelAdmin):

    class Meta:
        model = SiteCustomization


class SiteUrlsAdmin(admin.ModelAdmin):
    list_display = ["name", "url"]
    fieldsets = [
                (None, {"fields": ["name", "url"]}),
            ]

    class Meta:
        model = SiteUrls


class SiteSocialUrlsAdmin(admin.ModelAdmin):
    list_display = ["name", "url", "icon"]
    fieldsets = [
                (None, {"fields": ["name", "url", "icon"]}),
            ]

    class Meta:
        model = SiteSocialUrls


class FileUploadAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "publishing_date"]
    list_filter = ["publishing_date"]
    search_fields = ["name", "description"]
    fieldsets = [
                (None, {"fields": ["name", "description", "file"]}),
            ]

    class Meta:
        model = FileUpload


class OrganogramAdmin(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = [
                (None, {"fields": ["title", "slug", "description", "contents"]}),
            ]

    class Meta:
        model = Organogram


admin.site.register(SharedCategories, SharedTagsAdmin)
admin.site.register(SiteCustomization, SiteCustomizationAdmin)
admin.site.register(SiteUrls, SiteUrlsAdmin)
admin.site.register(SiteSocialUrls, SiteSocialUrlsAdmin)
admin.site.register(FileUpload, FileUploadAdmin)
admin.site.register(Organogram, OrganogramAdmin)
