from django import forms
from django.forms import ModelForm
from collec_management.models import Collec
from django import forms
from .models import Element

class CollecForm(ModelForm):
    class Meta:
        model = Collec
        fields = ["title", "description"]
        labels = {
            "title" :  "Title",
            "description" :  "Description"
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ['title', 'description', 'value', 'quantity', 'date', 'collection']