from django.shortcuts import render,redirect
from . import forms 
from . import models
# Create your views here.
def add_task(req):
    if req.method == 'POST':
        task_form = forms.taskForm(req.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    else:
        task_form = forms.taskForm()
    return render(req, 'add_task.html', {'form': task_form})


def edit_task(req, id):
    task = models.Task.objects.get(pk=id)
    task_form = forms.taskForm(instance=task)

    if req.method == 'POST':
        task_form = forms.taskForm(req.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    return render(req, 'add_task.html', {'form': task_form})

def delete_task(req, id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('home')

