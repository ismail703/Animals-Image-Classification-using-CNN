from django import forms
from .models import Image

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('image',)
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': "image"}),
        }
        labels = {
            'image': '',
        }

