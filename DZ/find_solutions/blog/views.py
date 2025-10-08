from django.shortcuts import render
from django.views.generic import ListView  # вывод в цикле
from .models import *


# Create your views here.

class BlogHome(ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        return context
