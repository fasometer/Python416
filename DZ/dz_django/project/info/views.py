from django.shortcuts import render, get_object_or_404

from .models import Info


# Create your views here.
def info_general(request):
    info = Info.objects.order_by('-date')
    return render(request, "info/info_general.html", {'info': info})


def info_details(request, info_id):
    info_d = get_object_or_404(Info, pk=info_id)
    return render(request, "info/info_details.html", {'info_d': info_d})



