from django.db import models
from category.models import Category
# from . import forms

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50) 
    description = models.TextField()
    category = models.ManyToManyField(Category)
    assgine_date = models.DateField()
    is_complete = models.BooleanField()

    def __str__(self):
        return self.title
    

    # birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
