from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile


class UserProfileAdmin(UserAdmin):

    list_display = ["username", "name", "surname", "is_staff", "date_joined", "last_login"]
    list_filter = ["is_staff", "is_active", "date_joined"]
    search_fields = ["username", "name", "surname", "email"]
    filter_horizontal = ["groups", "user_permissions"]
    fieldsets = [
            (None, {
                "fields": ["username", "password"],
                }),
            ("Users' data", {
                "fields": ["name", "surname", "email"],
                }),
            ("Permissions", {
                "fields": ["is_active", "is_staff", "is_superuser", "groups", "user_permissions"],
            }),
            ("Important dates", {
                "fields": ["last_login", "date_joined"],
                }),
        ]

    class Meta:
        model = UserProfile


#admin.site.register(UserProfile, UserProfileAdmin)