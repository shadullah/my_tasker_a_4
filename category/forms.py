from django import forms
from . models import Category

class categoForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
