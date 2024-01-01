from django import forms
from . models import Task

class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        # fields = ['title',  'description']
        widgets = {
            'assgine_date': forms.DateInput(attrs={'type': 'date'}),
        }