from django import forms
from .models import ShortModel

class UrlForm(forms.ModelForm):
    class Meta:
        model = ShortModel
        fields = ["long_url"]  
