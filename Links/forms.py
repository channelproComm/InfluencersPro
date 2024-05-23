from django.forms import ModelForm
from .models import Links

class LinksForm(ModelForm):
    class Meta:
        model=Links
        fields='__all__'
