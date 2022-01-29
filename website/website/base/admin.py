from django.contrib import admin

from abstracts.admin import TagBaseAdmin
from .models import SharedTag


class SharedTagAdmin(TagBaseAdmin):

    class Meta:
        model = SharedTag


admin.site.register(SharedTag, SharedTagAdmin)