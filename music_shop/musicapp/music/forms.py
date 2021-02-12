from django import forms
from .models import Cd

class CdCreate(forms.ModelForm):
    class Meta:
        model = Cd
        fields = '__all__'