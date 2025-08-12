from django.forms import ModelForm
from .models import Task
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'memo', 'memo_images', 'decision', 'decision_images', 'important', 'lines']
        widgets = {'lines': forms.Select()}

