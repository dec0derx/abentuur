from django.shortcuts import render

from .forms import FootageUploadForm


def upload_footage(request):
    saved = False
    if request.method == 'POST':
        form = FootageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved = True
            form = FootageUploadForm()
    else:
        form = FootageUploadForm()

    return render(request, 'uploads/upload.html', {'form': form, 'saved': saved})
