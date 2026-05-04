from django.contrib import admin

from .models import FootageUpload


@admin.register(FootageUpload)
class FootageUploadAdmin(admin.ModelAdmin):
    list_display = ('email', 'project_name', 'submitted_at')
    search_fields = ('email', 'name', 'project_name')
