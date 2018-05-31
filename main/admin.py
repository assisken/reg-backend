from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('sub', 'family_name', 'given_name', 'middle_name', 'email', 'email_verified',)
    ordering = ('sub',)
    list_filter = ('email_verified',)
