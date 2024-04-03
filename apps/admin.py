from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.models import Contact


# Register your models here.

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'location', 'email', 'number')
    search_fields = ['number']
