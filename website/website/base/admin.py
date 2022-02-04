from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from abstracts.admin import TagBaseAdmin
from .models import SharedTags, SiteCustomization, FileUpload, SiteUrls, SiteSocialUrls
from .forms import FlatPageForm


# class FlatPageAdmin(FlatPageAdmin):
#     """
#     Page Admin
#     """
#     form = FlatPageForm


class SharedTagsAdmin(TagBaseAdmin):

    class Meta:
        model = SharedTags


class SiteUrlsAdmin(admin.ModelAdmin):
    list_display = ["name", "url"]

    class Meta:
        model = SiteUrls


class SiteSocialUrlsAdmin(admin.ModelAdmin):
    list_display = ["name", "url", "social_icon"]

    class Meta:
        model = SiteSocialUrls


class SiteCustomizationAdmin(admin.ModelAdmin):

    class Meta:
        model = SiteCustomization


class FileUploadAdmin(admin.ModelAdmin):

    class Meta:
        model = FileUpload


admin.site.register(SharedTags, SharedTagsAdmin)
admin.site.register(SiteCustomization, SiteCustomizationAdmin)
admin.site.register(SiteUrls, SiteUrlsAdmin)
admin.site.register(SiteSocialUrls, SiteSocialUrlsAdmin)
admin.site.register(FileUpload, FileUploadAdmin)
#admin.site.register(FlatPage, FlatPageAdmin)