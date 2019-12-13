from django import forms
from  .models import Publisher,Article

class PublisherForm(forms.ModelForm):
    class Meta:
        model=Publisher
        fields="__all__"
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields="__all__"
