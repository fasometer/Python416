from django.shortcuts import render
from .models import Show


# Create your views here.

def index(request):
    language_prog = Show.objects.all()
    return render(request, 'show/index.html', {'language_prog': language_prog})
