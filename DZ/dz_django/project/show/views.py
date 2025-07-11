from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Show


# Create your views here.

def index(request):
    language_prog = Show.objects.all()
    return render(request, 'show/index.html', {'language_prog': language_prog})


def reg_user(request):
    if request.method == "GET":
        return render(request, 'show/reguser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'show/reguser.html', {'form': UserCreationForm(), 'error':'Такое имя уже есть. Задайте другое'})
        else:
            return render(request, 'show/reguser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})
