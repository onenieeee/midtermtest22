# forms.py
from django import forms
from .models import Animals

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = ['code', 'name', 'gene', 'image']
