from django.contrib import admin
from .models import Database


@admin.register(Database)
class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('pname', 'name', 'owner')
    ordering = ('pname',)
    exclude = ('pname',)


