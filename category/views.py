from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def add_category(req):
    if req.method=='POST':
        categoForm = forms.categoForm(req.POST)
        if categoForm.is_valid():
            categoForm.save()
            return redirect('home')
    else:
        categoForm = forms.categoForm()
    return render(req, 'add_category.html', {'form': categoForm})