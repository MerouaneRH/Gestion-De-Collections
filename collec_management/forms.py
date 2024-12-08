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
        fields = ['title', 'description', 'value', 'quantity', 'collection']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'collection': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Récupère l'utilisateur connecté
        super(ElementForm, self).__init__(*args, **kwargs)
        if user:
            # Filtre les collections pour ne montrer que celles appartenant à l'utilisateur connecté
            self.fields['collection'].queryset = Collec.objects.filter(user=user)
