from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm, MessageForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .utils import search_task
from django.contrib import messages


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


@login_required
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


@login_required
def current_tasks(request):
    tasks = Task.objects.filter(user=request.user, data_complete__isnull=True)
    return render(request, 'tasks/currenttasks.html', {'tasks': tasks})


@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'tasks/createtask.html', {'form': TaskForm()})
    else:
        try:
            form = TaskForm(request.POST, request.FILES)
            new_task = form.save(commit=False)
            # new_task.user = request.user
            new_task.decision = ''

            new_task.save()
            return redirect('currenttasks')
        except ValueError:
            return render(request, 'tasks/createtask.html', {'form': TaskForm(), 'error': 'Переданы неверные данные'})


@login_required
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


@login_required
def complete_task(request, tasks_pk):
    task = get_object_or_404(Task, pk=tasks_pk, user=request.user)
    if request.method == "POST":
        task.data_complete = timezone.now()
        task.save()
        return redirect('completedtasks')


@login_required
def completed_tasks(request):
    search_query, ts = search_task(request)
    # tasks = Task.objects.filter(user=request.user, data_complete__isnull=False).order_by('-data_complete')
    contex = {
        'tasks': ts,
        'search_query': search_query,
    }
    return render(request, 'tasks/completedtasks.html', contex)


@login_required
def delete_task(request, tasks_pk):
    task = get_object_or_404(Task, pk=tasks_pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('currenttasks')


@login_required(login_url='login')
def inbox(request):
    profile = request.user
    message_request = profile.messages.all()
    unread_count = message_request.filter(is_read=False).count()

    recipient = User.username
    form = MessageForm()

    try:
        sender = request.user
    except:
        sender = None

    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, "Yuor message was send")
            return redirect('inbox')
    #
    # context = {
    #     'recipient': recipient,
    #     'form': form,
    #     'message': message
    # }
    context = {
        'message_request': message_request,
        'unread_count': unread_count,
        'recipient': recipient,
        'form': form,
        # 'message': message
    }
    return render(request, 'tasks/inbox.html', context)


@login_required(login_url='login')
def veiw_message(request, pk):
    profile = request.user
    message = profile.messages.get(id=pk)
    if message.is_read is False:
        message.is_read = True
        message.save()
    context = {
        'message': message
    }

    # recipient = User.objects.get(id=pk)
    # form = MessageForm()
    #
    # try:
    #     sender = request.user.profile
    # except:
    #     sender = None
    #
    # if request.method == "POST":
    #     form = MessageForm(request.POST)
    #     if form.is_valid():
    #         message = form.save(commit=False)
    #         message.sender = sender
    #         message.recipient = recipient
    #
    #         if sender:
    #             message.name = sender.name
    #             message.email = sender.email
    #         message.save()
    #
    #         messages.success(request, "Yuor message was send")
    #         return redirect('user_profile', pk=recipient.id)
    #
    # context = {
    #     'recipient': recipient,
    #     'form': form,
    #     'message': message
    # }
    return render(request, 'tasks/message.html', context)
