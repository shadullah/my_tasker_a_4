from django.shortcuts import render,redirect
from . import forms 
# Create your views here.
def add_task(req):
    if req.method == 'POST':
        task_form = forms.taskForm(req.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form = forms.taskForm()
    return render(req, 'add_task.html', {'form': task_form})