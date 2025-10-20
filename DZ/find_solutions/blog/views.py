from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView  # вывод в цикле
from django.urls import reverse_lazy
from .forms import *
from .models import *


# Create your views here.

class BlogHome(ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True).select_related('cat')


class ShowPost(DetailView):
    model = Blog
    template_name = "blog/post.html"
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = [context['post']]
        return context


class BlogCategory(ListView):
    model = Blog
    template_name = "blog/index.html"
    context_object_name = 'posts'

    def get_queryset(self):
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Категория - " + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = "blog/addpage.html"
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Добавить статью"
        return context
