from django import forms
from .models import Muscian

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Muscian
        fields = ['first_name', 'last_name', 'instrument']
