# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = [
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "group_membership",
    ]
    list_filter = [
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "groups",
    ]
    readonly_fields = [
        "last_login",
        "date_joined",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = [
        "email",
    ]
    ordering = [
        "email",
    ]

    @admin.display(empty_value="???")
    def group_membership(self, obj):
        return ", ".join(str(g) for g in obj.groups.all())
