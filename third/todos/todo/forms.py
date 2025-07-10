from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):
    class Meta:  # всегда тлько так внутрназвание
        model = Todo
        fields = ['title', 'memo', 'important']

