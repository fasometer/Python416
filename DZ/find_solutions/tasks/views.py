from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


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
    return render(request, 'tasks/currenttasks.html')
