from django import forms

from .models import FootageUpload


class FootageUploadForm(forms.ModelForm):
    class Meta:
        model = FootageUpload
        fields = [
            'name',
            'email',
            'phone',
            'project_name',
            'notes',
            'footage_file',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number (optional)'}),
            'project_name': forms.TextInput(attrs={'placeholder': 'Project name (required for file organization)'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Notes for the edit', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make project_name required since it's used for folder organization
        self.fields['project_name'].required = True
