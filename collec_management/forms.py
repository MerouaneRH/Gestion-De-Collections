from django.forms import ModelForm
from collec_management.models import Collec

class CollecForm(ModelForm):
    class Meta:
        model = Collec
        fields = ["title", "description"]
        labels = {
            "title" :  "Title",
            "description" :  "Description"
        }