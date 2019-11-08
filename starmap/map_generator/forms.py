from django import forms
from .models import Starmap
from .choices import MAP_TYPE_CHOICES


class StarmapForm(forms.ModelForm):
    

    class Meta:
        model = Starmap
        fields = ['date', 'text','city', 'map_type']
        widgets = {
            'map_type': forms.Select(choices=MAP_TYPE_CHOICES,attrs={'class': 'form-control'}),
        }