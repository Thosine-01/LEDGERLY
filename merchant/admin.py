from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Merchant


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Merchant", {"fields": ("merchant",)}),
    )
    list_display = ["username", "email", "merchant", "is_staff"]


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]