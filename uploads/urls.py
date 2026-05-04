from django.urls import path

from .views import upload_footage

app_name = 'uploads'

urlpatterns = [
    path('', upload_footage, name='upload_footage'),
]
