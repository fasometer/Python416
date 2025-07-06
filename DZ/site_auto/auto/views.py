from django.shortcuts import render

from auto.models import Automat


# Create your views here.
def index(request):
    company = Automat.objects.all()
    return render(request, 'auto/index.html', {'company': company})
