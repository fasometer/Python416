from django.forms import ModelForm
from .models import Task
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'lines', 'place', 'memo', 'memo_images', 'decision', 'decision_images', 'important']
        widgets = {'lines': forms.Select()}
