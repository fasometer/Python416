from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError


# Create your views here.
def home(request):
    return render(request, 'todo/home.html')


def signup_user(request):
    if request.method == "GET":
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()  # сохраням пользователя
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'Такое имя уже есть. Задайте другое'})
        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def current_todos(request):
    return render(request, 'todo/currenttodos.html')


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
