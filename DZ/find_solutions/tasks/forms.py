from django.forms import ModelForm
from .models import Task
from django import forms

f = (
    ('1', 'PK1'),
    ('2', 'PK2'),
    ('3', 'PK3'),

)


class TaskForm(ModelForm):
    liens = forms.ChoiceField(choices=f)

    class Meta:
        model = Task
        fields = ['title', 'memo', 'memo_images', 'decision', 'decision_images', 'important','line']
