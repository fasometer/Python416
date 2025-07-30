from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone


# Create your views here.

def home(request):
    return render(request, 'tasks/home.html')


def signup_user(request):
    if request.method == "GET":
        return render(request, "tasks/signupuser.html", {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()  # сохраням пользователя
                login(request, user)
                return redirect('currenttasks')
            except IntegrityError:
                return render(request, 'tasks/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'Такое имя уже есть. Задайте другое'})
        else:
            return render(request, 'tasks/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def login_user(request):
    if request.method == "GET":
        return render(request, 'tasks/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'tasks/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('currenttasks')


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def current_tasks(request):
    tasks = Task.objects.filter(user=request.user, data_complete__isnull=True)
    return render(request, 'tasks/currenttasks.html', {'tasks': tasks})


def create_task(request):
    if request.method == "GET":
        return render(request, 'tasks/createtask.html', {'form': TaskForm()})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('currenttasks')
        except ValueError:
            return render(request, 'tasks/createtask.html', {'form': TaskForm(), 'error': 'Переданы неверные данные'})


def view_task(request, tasks_pk):
    task = get_object_or_404(Task, pk=tasks_pk)
    if request.method == "GET":
        form = TaskForm(instance=task)
        return render(request, 'tasks/viewtask.html', {'task': task, 'form': form})
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('currenttasks')
        except ValueError:
            return render(request, 'tasks/viewtask.html', {'task': task, 'form': form, 'error': "Неверные данные"})


def complete_task(request, tasks_pk):
    task = get_object_or_404(Task, pk=tasks_pk, user=request.user)
    if request.method == "POST":
        task.data_complete = timezone.now()
        task.save()
        return redirect('currenttasks')


def completed_tasks(request):
    tasks = Task.objects.filter(user=request.user, data_complete__isnull=False).order_by('-data_complete')
    return render(request, 'tasks/completedtasks.html', {'tasks': tasks})
