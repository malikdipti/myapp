from django import forms
from .models import BiriyaniCatModel
from .models import BiriyaniModel

class BiriyaniCatFrom(forms.ModelForm):
    class Meta:
        model=BiriyaniCatModel
        fields="__all__"
class BiriyaniForm(forms.ModelForm):
    class Meta:
        model=BiriyaniModel
        fields="__all__"