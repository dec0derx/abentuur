from django.db import models
from django.utils.text import slugify


def footage_upload_path(instance, filename):
    # Use project_name if available, otherwise use name, otherwise use 'untitled'
    folder_name = instance.project_name or instance.name or 'untitled'
    # Clean the folder name to be filesystem-safe
    safe_folder = slugify(folder_name)[:100] or 'untitled'
    return f'footage/{safe_folder}/{filename}'


class FootageUpload(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    project_name = models.CharField(max_length=150)  # Made required for folder organization
    notes = models.TextField(blank=True)
    footage_file = models.FileField(upload_to=footage_upload_path, blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project_name or 'Footage upload'} — {self.email}"
