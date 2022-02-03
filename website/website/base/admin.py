from django.contrib import admin

from abstracts.admin import TagBaseAdmin
from .models import SharedTags


class SharedTagsAdmin(TagBaseAdmin):

    class Meta:
        model = SharedTags


admin.site.register(SharedTags, SharedTagsAdmin)