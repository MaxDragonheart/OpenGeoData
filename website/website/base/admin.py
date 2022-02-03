from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from abstracts.admin import TagBaseAdmin
from .models import SharedTags, SiteCustomization, FileUpload
from .forms import FlatPageForm


# class FlatPageAdmin(FlatPageAdmin):
#     """
#     Page Admin
#     """
#     form = FlatPageForm


class SharedTagsAdmin(TagBaseAdmin):

    class Meta:
        model = SharedTags


class SiteCustomizationAdmin(admin.ModelAdmin):

    class Meta:
        model = SiteCustomization


class FileUploadAdmin(admin.ModelAdmin):

    class Meta:
        model = FileUpload


admin.site.register(SharedTags, SharedTagsAdmin)
admin.site.register(SiteCustomization, SiteCustomizationAdmin)
admin.site.register(FileUpload, FileUploadAdmin)
#admin.site.register(FlatPage, FlatPageAdmin)