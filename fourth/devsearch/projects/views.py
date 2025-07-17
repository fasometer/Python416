from django.shortcuts import render


# Create your views here.

def projects(requwest):
    return render(requwest, "projects/projects.html")
